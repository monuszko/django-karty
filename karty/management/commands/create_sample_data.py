# -*- coding: utf-8
import random
from faker import Faker

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from karty.factories import MenuCardFactory, DishFactory

fake = Faker()
tzinfo = timezone.get_default_timezone()

DISH_COUNTS = (
        10, 15, 21, 16, 0, 0, 9, 5, 44, 28, 13, 0, 81, 33, 20, 19, 18, 0, 12, 
        0, 8, 14, 36, 0, 11, 0, 0, 0, 17, 14, 10, 10, 10, 12, 13, 0, 15, 0,
        17, 18, 13, 29, 4, 21, 33, 11, 23, 11, 9, 38, 15, 26, 21, 35, 36, 16,
        37, 7, 25, 11, 0, 32, 16, 13, 24, 11, 19, 28, 36, 22, 15, 26, 8, 13,
        10, 8, 40, 31, 24, 5, 35, 25, 2, 15, 38, 32, 0, 40, 20, 20, 8, 14, 4,
        38, 10, 0, 24, 40, 27, 6, 12, 33, 9, 19, 4, 6, 12, 8, 35, 26, 22, 4, 2,
        11, 28, 26, 33, 34, 6, 17, 16, 19, 25, 30, 7, 24, 40, 38, 9, 0, 16, 2,
        20, 17, 32, 0, 16, 8, 37, 10, 5, 17, 40, 40, 39, 34, 11, 40, 35, 5, 16,
        31, 31, 3, 37, 7, 18, 26, 6, 32, 31, 6, 38, 0, 21, 29, 9, 28, 23, 30,
        40, 12, 36, 6, 16, 3, 31, 34, 0, 8, 12, 11, 2, 18, 37, 0, 8, 3, 16, 15,
        34, 25, 18, 24, 17, 13, 16, 37, 27, 36, 14, 34, 32, 13, 13, 22, 16, 21,
        10, 2, 9, 31, 21, 33, 32, 10, 13, 10, 29, 20, 7, 5, 36, 34, 40, 31, 38,
        29, 5, 33, 31, 18, 34, 19, 19, 36, 8, 14, 19, 20,
)

class Command(BaseCommand):
    help = "Populates the database with sample data to illustrate the app."

    def handle(self, *args, **options):
        for dish_count in DISH_COUNTS:

            pub_date = fake.date_time_this_year(
                    before_now=True, after_now=False, tzinfo=tzinfo)
            mod_date = pub_date
            if random.random() < 0.4:
                mod_date = fake.date_time_between(
                        start_date=pub_date, end_date='now', tzinfo=tzinfo)

            card = MenuCardFactory(pub_date=pub_date, mod_date=mod_date)
            DishFactory.create_batch(dish_count, menucard=card)

