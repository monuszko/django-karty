# -*- coding: utf-8
from django.core.management.base import BaseCommand, CommandError

from karty.factories import MenuCardFactory, DishFactory


class Command(BaseCommand):
    help = "Populates the database with sample data to illustrate the app."

    def handle(self, *args, **options):
        for dish_count in (10, 15, 21, 16, 0, 0, 9, 5, 44, 28, 13, 0, 81, 33,
                20, 19, 18, 0, 12, 0, 8, 14, 36, 0, 11, 0, 0, 0, 17, 14, 10,
                10, 10, 12, 13, 0, 15, 0, 17, 18):
            card = MenuCardFactory()
            DishFactory.create_batch(dish_count, menucard=card)

