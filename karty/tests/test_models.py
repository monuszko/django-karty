import datetime

from django.test import TestCase
from django.utils import timezone

from karty.factories import MenuCardFactory


class MenuCardTests(TestCase):
    def test_was_modified_in_near_future(self):
        """
        was_modifed() should return False for MenuCard
        whose mod_date is in the near future.
        """
        pub_date = timezone.now()
        mod_date = timezone.now() + datetime.timedelta(minutes=3)
        future_menucard = MenuCardFactory(pub_date=pub_date, mod_date=mod_date)

        self.assertIs(future_menucard.was_modified(), False)

    def test_was_modified_in_far_future(self):
        """
        was_modifed() should return False for MenuCard
        whose mod_date is in the far future.
        """
        pub_date = timezone.now()
        mod_date = timezone.now() + datetime.timedelta(days=5233)
        future_menucard = MenuCardFactory(pub_date=pub_date, mod_date=mod_date)

        self.assertIs(future_menucard.was_modified(), False)

    def test_was_modified_few_minutes_after_publication(self):
        """
        was_modifed() should return False for MenuCard
        whose mod_date is within trivial period after publication.
        """
        pub_date = timezone.now() - datetime.timedelta(days=15)
        mod_date = pub_date + datetime.timedelta(minutes=3)

        past_menucard = MenuCardFactory(pub_date=pub_date, mod_date=mod_date)

        self.assertIs(past_menucard.was_modified(), False)

    def test_was_modified_long_after_publication(self):
        """
        was_modifed() should return True for MenuCard
        whose mod_date is meanigful amount of time after publication.
        """
        pub_date = timezone.now() - datetime.timedelta(days=15)
        mod_date = pub_date + datetime.timedelta(minutes=36)

        past_menucard = MenuCardFactory(pub_date=pub_date, mod_date=mod_date)

        self.assertIs(past_menucard.was_modified(), True)
