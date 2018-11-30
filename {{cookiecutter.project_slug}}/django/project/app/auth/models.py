import logging
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.utils.translation import ugettext_lazy as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from . managers import UserManager

log = logging.getLogger(__name__)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Create a more flexible default User class.

    Notes:
        - Does not implement username
        - Uses email instead of username as unique identifier
        - Provides more contemporary "full_name" field
        - Maintains is_active
        - Provides more semantic is_admin field (is_staff returns this prop. for compat.)
        - Provides created (instead of date_joined) field
        - Provides last modified field

    Resources:
        - http://bit.ly/custom-django-user
        - https://docs.djangoproject.com/en/dev/topics/auth/customizing/#a-full-example

    """

    # NOTE: Non-standard: Used by admin.UserAdmin
    #       Placed in the model (in lieu of admin) so these settings
    #       can be more easily customized and so they are also
    #       closer in proximity to actual field definitions.
    ADMIN_ORDERING = ("email", )
    ADMIN_NONE_FIELDSET = ("created", "modified", "email", "password", )
    ADMIN_FLAGS_FIELDSET = ("is_active", "is_admin", "is_superuser")
    ADMIN_PERMISSION_FIELDSET = ("groups", "user_permissions")
    ADMIN_INFO_FIELDSET = ("full_name", )
    ADMIN_LIST_DISPLAY_FIELDSET = ("email", "full_name", ) + ADMIN_FLAGS_FIELDSET
    ADMIN_LIST_FILTER_FIELDSET = ADMIN_FLAGS_FIELDSET
    ADMIN_SEARCH_FIELDSET = ("email", )
    ADMIN_FILTER_HORIZONTAL_FIELDSET = ()
    ADMIN_READONLY_FIELDS = ("created", "modified", )

    created = AutoCreatedField(_("Created"))
    modified = AutoLastModifiedField(_("Modified"))
    email = models.EmailField(
        verbose_name=_("Email Address"), max_length=255, unique=True)
    full_name = models.CharField(
        verbose_name=_("Full Name"), max_length=255, blank=True)
    is_active = models.BooleanField(
        verbose_name=_("Is Active"), default=True,
        help_text=_(
            "Indicates whether the user is considered 'active'. "
            "Use this to deactivate accounts instead of deleting them"
        )
    )
    is_admin = models.BooleanField(
        verbose_name=_("Is Admin"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site.")
    )

    objects = UserManager()

    # NOTE: Required,
    #       String describing the field used as the unique identifier.
    USERNAME_FIELD = "email"

    # NOTE: Required,
    #       Field names to be prompted when using the createsuperuser management command;
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    # NOTE: Required method
    def get_full_name(self):
        return self.full_name

    # NOTE: Required method
    def get_short_name(self):
        return self.full_name

    def __str__(self):
        return self.email

    # NOTE: Compat, proxy is_admin as is_staff
    @property
    def is_staff(self):
        return self.is_admin


class UserGroup(Group):
    """A simple passthrough allowing registration Group with this app."""

    class Meta:
        proxy = True
        verbose_name = _("User Group")
        verbose_name_plural = _("User Groups")
