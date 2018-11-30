from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """Create a default custom user."""

    help = "Create default superuser without prompts."

    def handle(self, *args, **options):
        User = get_user_model()
        email = "admin@example.com"
        full_name = "Admin"
        password = "pass"
        exists = User.objects.filter(email=email).exists()

        if not exists:
            User.objects.create_superuser(email=email, password=password, full_name=full_name)
        else:
            self.stdout.write(f"Admin user with {email} exists, skipping...")
