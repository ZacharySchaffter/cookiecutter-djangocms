import logging
from django.contrib.auth.base_user import BaseUserManager


log = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    """Custom manager for the models.User."""

    def user_factory(self, email, password, **kwargs):
        """Create a parameterized user."""
        if not email:
            return ValueError("User email is required.")
        if not password:
            return ValueError("User password is required.")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **kwargs):
        kwargs.setdefault("is_admin", False)
        kwargs.setdefault("is_superuser", False)
        return self.user_factory(email, password, **kwargs)

    def create_superuser(self, email=None, password=None, **kwargs):
        kwargs.setdefault("is_admin", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.user_factory(email, password, **kwargs)

