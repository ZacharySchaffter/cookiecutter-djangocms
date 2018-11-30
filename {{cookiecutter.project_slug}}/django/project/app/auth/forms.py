from django import forms
from django.contrib import admin
from django.contrib.auth import password_validation
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from .models import User


class UserCreationForm(forms.ModelForm):
    """
    A custom form for creating models.User.

    Notes:
        - Only requires a single password (i.e., no confirmation)

    """
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = "__all__"
        labels = {
            # NOTE: Updating this here to avoid patching PermissionsMixin
            "is_superuser": _("Is Superuser"),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean_password(self):
        password = self.cleaned_data.get("password")
        user = self.instance
        password_validation.validate_password(password, user)
        return password


class UserChangeForm(forms.ModelForm):
    """A custom form for updating models.User."""
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password/\">this form</a>."
        ),
    )

    class Meta:
        model = User
        fields = "__all__"
        labels = {
            # NOTE: Updating this here to avoid patching PermissionsMixin
            "is_superuser": _("Is Superuser"),
        }

    def clean_password(self):
        # NOTE: Users cannot change the password via this form,
        #       so always return the initial value.
        return self.initial["password"]
