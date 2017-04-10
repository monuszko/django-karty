from django.test import TestCase
from django.core.management import call_command

from karty.factories import MenuCardFactory, DishFactory
from karty.models import MenuCard, Dish
from karty.management.commands.create_sample_data import DISH_COUNTS


class CommandTests(TestCase):
    def test_create_sample_data(self):
        """
        Test that sample data is created with specified counts.
        """

        args = []
        kwargs = {}
        call_command('create_sample_data', *args, **kwargs)

        self.assertEqual(MenuCard.objects.all().count(), len(DISH_COUNTS))
        for card, nb_dishes in zip(MenuCard.objects.all(), DISH_COUNTS):
            self.assertEqual(card.dishes.count(), nb_dishes)

    def test_destroy_app_data(self):
        """
        All objects from the 'karty' app should be gone.
        """
        for x in range(4):
            MenuCardFactory()

        self.assertEqual(MenuCard.objects.all().count(), 4)

        for y in range(7):
            DishFactory()

        self.assertEqual(Dish.objects.all().count(), 7)

        args = []
        kwargs = {}
        call_command('destroy_app_data', *args, **kwargs)

        self.assertEqual(MenuCard.objects.all().count(), 0)
        self.assertEqual(Dish.objects.all().count(), 0)

