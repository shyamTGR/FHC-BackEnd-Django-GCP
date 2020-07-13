from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
class Command(BaseCommand):
  def handle(self, *args, **options):
    User = get_user_model()
    if not User.objects.filter(username="shyam639").exists():
        User.objects.create_superuser("shyam639", "admin@gmail.com", "Christ@123")