from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create a superuser, admin, without prompts"

    def handle(self, *args, **options):
        """
        Create a superuser without prompts.
        Notes:
            * Skips creation if user, admin, already exists.
        """
        user_name = "admin"
        user_pass = "pass"
        user_email = "admin@local.com"

        user, created = User.objects.get_or_create(
            username=user_name, email=user_email, is_superuser=True,
            is_staff=True)

        if created:
            user.set_password(user_pass)
            user.save()
            self.stdout.write(
                "Created user: {user_name}\n".format(user_name=user_name))
        else:
            self.stdout.write(
                "User exists, skipping...\n"
            )
