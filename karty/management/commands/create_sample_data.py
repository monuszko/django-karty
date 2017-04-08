# -*- coding: utf-8
import random
from unittest.mock import patch
from faker import Faker

from django.core.management.base import BaseCommand, CommandError

from karty.factories import MenuCardFactory, DishFactory

fake = Faker()

class Command(BaseCommand):
    help = "Populates the database with sample data to illustrate the app."

    def handle(self, *args, **options):
        for dish_count in (10, 15, 21, 16, 0, 0, 9, 5, 44, 28, 13, 0, 81, 33,
                20, 19, 18, 0, 12, 0, 8, 14, 36, 0, 11, 0, 0, 0, 17, 14, 10,
                10, 10, 12, 13, 0, 15, 0, 17, 18):

            pub_date = fake.date_time_this_year(
                    before_now=True, after_now=False)
            mod_date = pub_date
            if random.random() < 0.4:
                mod_date = fake.date_time_between(
                        start_date=pub_date, end_date='now')

            with patch('django.utils.timezone.now') as mock_now:
                mock_now.return_value = mod_date
                card = MenuCardFactory(pub_date=pub_date)
                DishFactory.create_batch(dish_count, menucard=card)

