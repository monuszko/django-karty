# -*- coding: utf-8
from django.core.management.base import BaseCommand, CommandError

from karty.factories import MenuCardFactory, DishFactory


class Command(BaseCommand):
    help = "Populates the database with sample data to illustrate the app."

    def handle(self, *args, **options):
        card1 = MenuCardFactory()
        card1.save()

        for x in range(5):
            dish = DishFactory(menucard=card1, price=5)
            dish.save()

        card2 = MenuCardFactory()
        card2.save()

        for x in range(11):
            dish = DishFactory(menucard=card2, price=5)
            dish.save()
