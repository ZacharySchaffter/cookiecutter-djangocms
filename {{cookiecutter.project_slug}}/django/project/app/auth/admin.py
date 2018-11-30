import logging
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin, GroupAdmin as BaseGroupAdmin)
from django.utils.translation import ugettext_lazy as _
from .models import User, UserGroup
from .forms import UserCreationForm, UserChangeForm


log = logging.getLogger(__name__)


def fieldset_factory(label, fieldset, **kwargs):
    return (
        label, {
            **kwargs,
            "fields": fieldset,
        },
    )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    ordering = User.ADMIN_ORDERING
    list_display = User.ADMIN_LIST_DISPLAY_FIELDSET
    list_filter = User.ADMIN_LIST_FILTER_FIELDSET
    search_fields = User.ADMIN_SEARCH_FIELDSET
    readonly_fields = User.ADMIN_READONLY_FIELDS
    filter_horizontal = User.ADMIN_FILTER_HORIZONTAL_FIELDSET
    none_fields = fieldset_factory(None, User.ADMIN_NONE_FIELDSET)
    flag_fields = fieldset_factory(_("Flags"), User.ADMIN_FLAGS_FIELDSET)
    permission_fields = fieldset_factory(
        _("Permissions"), User.ADMIN_PERMISSION_FIELDSET, classes=("collapse", ))
    info_fields = fieldset_factory(_("Info"), User.ADMIN_INFO_FIELDSET)
    fieldsets = (none_fields, flag_fields, info_fields, permission_fields, )
    # NOTE: Non-standard prop, see: get_fieldsets in BaseUserAdmin
    #      i.e., django.django.contrib.auth.admin.UserAdmin
    add_fieldsets = (none_fields, flag_fields, info_fields, )


# Re-register admin with this app so relevant things sit together
admin.site.unregister(Group)


@admin.register(UserGroup)
class UserGroupAdmin(BaseGroupAdmin):
    """A simple passthrough allowing registration Group with this app."""
