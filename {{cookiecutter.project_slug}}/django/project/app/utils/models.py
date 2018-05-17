from django.db.models.fields import Field
import types


def patch_model(model_to_patch, class_to_patch_with):
    """
    Patch a Django model with additional/replacement fields/methods.

    * New fields/methods are added
    * Existing methods are replaced with <methodname>__overriden
    * Existing fields are deleted and replaced
    * Class used to patch must be an old-style class

    Arguments:
        model_to_patch: Source model
        class_to_patch_with: Override class

    Example:
    from django.contrib.auth.models import User
    from app.utils.patch import patch_model

    class UserOverride:
        email = models.EmailField(_("E-mail address"), unique=True)
        new_field = models.CharField(_("New field"), max_length=225)

        def save(self, *args, **kwargs):
            self.save__overriden(*args, **kwargs)

    patch_model(User, UserOverride)
    """
    # The _meta attribute is where the definition of the fields is stored in
    # django model classes.
    patched_meta = getattr(model_to_patch, '_meta')

    for name, obj in class_to_patch_with.__dict__.items():

        # If the attribute is a field, delete it if it already exists.
        if isinstance(obj, Field):
            index = -1
            for field_table in (patched_meta.local_fields,
                                patched_meta.local_many_to_many):
                for i in range(0, len(field_table)):
                    field = field_table[i]
                    if field.name == name:
                        index = i

                        # The creation_counter is used by django to know in
                        # which order the database columns are declared. We
                        # get it to ensure that when we override a field it
                        # will be declared in the same position as before.
                        creation_counter = field_table[i].creation_counter
                        break

                if index != -1:
                    field_table.pop(index)
                    obj.creation_counter = creation_counter
                    break

        elif isinstance(obj, types.FunctionType) or isinstance(obj, property):
            if getattr(model_to_patch, name, None):
                setattr(model_to_patch, name + '__overridden',
                        getattr(model_to_patch, name))

        # Add the new field/method name and object to the model.
        if not name.startswith("__"):
            model_to_patch.add_to_class(name, obj)


class CopyPluginRelationsMixin(object):
    """
    Provide a generic implementation of CMSPlugin.copy_relations.
    From DjangoCMS docs:
    Every time the page with your custom plugin is published
    the plugin is copied. If your custom plugin has any
    related models (ForeignKey, OneToOne, or ManyToMany)
    you are responsible for copying those related objects.
    This mixin provides a declarative, extensible
    implementation of copy_relations based on best
    practices described in the DjangoCMS documentation.
    See:
        * [DjangoCMS Handling Plugin Relations](https://bit.ly/2IfFnLm)
    Example:
        # app/foo/models.py
        class FooPlugin(CopyPluginRelationsMixin, CMSPlugin):
            # Additional model code omitted for berevity...
            copy_plugin_relations = {
                # (field_name, field_related_name)
                "foreign_key_from": (
                    ("plugin", "images"),
                ),
                # (field_name, field_related_name)
                "many_to_many_from": (
                    ("plugin", "tags")
                ),
                # (field_name, field_related_name)
                "one_to_one_from": (
                    ("plugin", "video")
                ),
            }
        class FooImages(models.Model):
            # Additional model code omitted for berevity...
            plugin = models.ForeignKey(
                FooPlugin, on_delete=models.CASCADE, related_name="images")
        class FooVideo(models.Model):
            # Additional model code omitted for berevity...
            plugin = models.OneToOne(
                FooPlugin, on_delete=models.CASCADE, related_name="video")
        class FooTags(models.Model):
            # Additional model code omitted for berevity...
            plugin = models.ManyToMany(
                FooPlugin, on_delete=models.CASCADE, related_name="video")
    Notes:
        * `self` in copy_relations is the "new instance" ready for publish
        * `field_name` refers to the related field
           (ForeignKey, ManyToMany, OneToOne) on the related model.
        * `field_related_name` refers to the value in `related_name`
           on the related field on the related model.
        * This class currently handles only relations _from_ other models
          (as shown in the example).
    """

    copy_plugin_relations = {
        "foreign_key_from": (),
        "many_to_many_from": (),
        "one_to_one_from": (),
    }

    def copy_relations(self, oldinstance):
        foreign_key_from = self.copy_plugin_relations.get("foreign_key_from", ())
        many_to_many_from = self.copy_plugin_relations.get("many_to_many_from", ())
        one_to_one_from = self.copy_plugin_relations.get("one_to_one_from", ())

        self.copy_foreign_key_from(
            config=foreign_key_from, draft_instance=oldinstance)
        self.copy_many_to_many_from(
            config=many_to_many_from, draft_instance=oldinstance)
        self.copy_one_to_one_from(
            config=one_to_one_from, draft_instance=oldinstance)

    def copy_foreign_key_from(self, config, draft_instance):
        for field_name, field_related_name in config:
            # Clear any previously copied instances
            delete_related_models(self, field_related_name)
            # Copy related models
            copy_related_models(draft_instance, self, field_name, field_related_name)

    def copy_many_to_many_from(self, config, draft_instance):
        for field_name, field_related_name in config:
            # Clear any previously copied instances
            delete_related_models(self, field_related_name)
            # Copy related models
            copy_related_models(draft_instance, self, field_name, field_related_name)

    def copy_one_to_one_from(self, config, draft_instance):
        for field_name, field_related_name in config:
            # Clear previous relation before copying
            old_copy = getattr(self, field_related_name, None)

            if old_copy:
                old_copy.delete()

            # Copy new version from draft
            to_copy_instance = getattr(draft_instance, field_related_name, None)

            if to_copy_instance:
                setattr(to_copy_instance, field_name, self)
                to_copy_instance.pk = None
                to_copy_instance.save()
