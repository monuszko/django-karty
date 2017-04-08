from django.core.management.base import BaseCommand, CommandError
from karty.models import MenuCard, Dish

class Command(BaseCommand):
    help = """Destroys all data in the app tables.
            Used to clean up after 'create_sample_data'."""

    def handle(self, *args, **options):
        MenuCard.objects.all().delete()
        Dish.objects.all().delete()
