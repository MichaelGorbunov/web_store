from django.core.management.base import BaseCommand
from django.core.management import call_command
from blog.models import Post


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Post.objects.all().delete()

        call_command("loaddata", "post_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
