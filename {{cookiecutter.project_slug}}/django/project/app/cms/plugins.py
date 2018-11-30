from app.shared.utils import copy_related_models, delete_related_models


class CopyPluginRelationsMixin:
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
            delete_related_models(self, field_related_name)
            copy_related_models(draft_instance, self, field_name, field_related_name)

    def copy_many_to_many_from(self, config, draft_instance):
        for field_name, field_related_name in config:
            delete_related_models(self, field_related_name)
            copy_related_models(draft_instance, self, field_name, field_related_name)

    def copy_one_to_one_from(self, config, draft_instance):
        for field_name, field_related_name in config:
            old_copy = getattr(self, field_related_name, None)

            if old_copy:
                old_copy.delete()

            to_copy_instance = getattr(draft_instance, field_related_name, None)

            if to_copy_instance:
                setattr(to_copy_instance, field_name, self)
                to_copy_instance.pk = None
                to_copy_instance.save()
