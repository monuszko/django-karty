# -*- coding: utf-8
from django.core.management.base import BaseCommand, CommandError

from karty.factories import MenuCardFactory, DishFactory


class Command(BaseCommand):
    help = "Populates the database with sample data to illustrate the app."

    def handle(self, *args, **options):
        for dish_count in (10, 15, 21, 16, 9, 5, 44, 28, 13, 81, 33, 20, 19,
                18, 12, 8, 14, 36, 11, 17, 14, 10, 10, 10, 12, 13, 15, 17, 18):
            card = MenuCardFactory()
            DishFactory.create_batch(dish_count, menucard=card)

