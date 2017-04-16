from faker import Faker

from django.test import TestCase
from django.utils import timezone

from karty.factories import MenuCardFactory, DishFactory
from karty.models import MenuCard, Dish

fake = Faker()
tzinfo = timezone.get_default_timezone()


class MenuCardFactoryTests(TestCase):
    def test_menucard_objects_are_created(self):
        """
        Test that calling factory results in new objects.
        """
        for x in range(13):
            MenuCardFactory()

        self.assertEqual(MenuCard.objects.all().count(), 13)

    def test_menucard_name_is_unique(self):
        """
        Name field should be generated unique.
        """
        names = set()
        num_menucards = 800
        for x in range(num_menucards):
            menucard = MenuCardFactory()
            names.add(menucard.name)

        self.assertEqual(len(names), num_menucards)

    def test_pub_date_is_assigned(self):
        """
        pub_date passed to the factory should be assigned to the object.
        """
        date = fake.date_time(tzinfo=tzinfo)
        menucard = MenuCardFactory(pub_date=date)

        self.assertEqual(menucard.pub_date, date) 

    def test_mod_date_is_assigned(self):
        """
        mod_date passed to the factory should be assigned to the object.
        """
        date = fake.date_time(tzinfo=tzinfo)
        menucard = MenuCardFactory(mod_date=date)

        self.assertEqual(menucard.mod_date, date) 


class DishFactoryTests(TestCase):
    def test_dish_objects_are_created(self):
        """
        Test that calling factory results in new objects.
        """
        for x in range(13):
            DishFactory()

        self.assertEqual(Dish.objects.all().count(), 13)

    def test_dish_name_is_unique(self):
        """
        Name field should be generated unique.
        """
        names = set()
        num_dishes = 800
        for x in range(num_dishes):
            dish = MenuCardFactory()
            names.add(dish.name)

        self.assertEqual(len(names), num_dishes)
