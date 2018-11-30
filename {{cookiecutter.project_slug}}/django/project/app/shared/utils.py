def copy_related_models(
        copy_from_instance, copy_to_instance, field_name, field_related_name):
    """Copy related models from one instance to another."""
    to_copy = getattr(
        copy_from_instance, field_related_name).order_by("pk").all()

    for related_instance in to_copy:
        # pk = None, instance.save()
        # is a standard pattern for copying django models.
        setattr(related_instance, field_name, copy_to_instance)
        related_instance.pk = None
        related_instance.save()


def delete_related_models(delete_from_instance, field_related_name):
    """Delete all related models from an instance."""
    getattr(delete_from_instance, field_related_name).all().delete()


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
