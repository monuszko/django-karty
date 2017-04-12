from django.test import Client, TestCase, override_settings
from django.urls import reverse

from karty.factories import MenuCardFactory, DishFactory


client = Client()


class MenuCardListTests(TestCase):
    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_view_with_no_menucards(self):
        """
        If no menucards exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('karty:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No menu cards are available")
        self.assertQuerysetEqual(response.context['page'], [])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_view_with_empty_menucard(self):
        """
        If menucard has no dishes, it is not displayed.
        """
        MenuCardFactory()

        response = self.client.get(reverse('karty:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No menu cards are available")
        self.assertQuerysetEqual(response.context['page'], [])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_view_with_two_empty_menucards(self):
        """
        If all menucards have no dishes, neither is displayed.
        """
        MenuCardFactory()
        MenuCardFactory()

        response = self.client.get(reverse('karty:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No menu cards are available")
        self.assertQuerysetEqual(response.context['page'], [])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_view_with_one_normal_menucard(self):
        """
        If there's one menucard with dishes, it is displayed.
        """
        m = MenuCardFactory()
        for x in range(5):
            DishFactory(menucard=m)

        response = self.client.get(reverse('karty:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, m.name)
        self.assertQuerysetEqual(response.context['page'],
                ['<MenuCard: %s>' % m.name])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_view_with_two_normal_menucards(self):
        """
        If there are two non-empty menucards, both are displayed.
        """
        m = MenuCardFactory(name='menu 1')
        n = MenuCardFactory(name='menu 2')
        for x in range(5):
            DishFactory(menucard=m)
        for x in range(5):
            DishFactory(menucard=n)

        response = self.client.get(reverse('karty:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, m.name)
        self.assertContains(response, n.name)
        self.assertQuerysetEqual(response.context['page'],
                ['<MenuCard: menu 1>', '<MenuCard: menu 2>'])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_view_with_one_normal_one_empty_menucard(self):
        """
        If two menucards exist, only the one with dishes is displayed.
        """
        m = MenuCardFactory(name='menu 1')
        n = MenuCardFactory(name='menu 2')
        for x in range(5):
            DishFactory(menucard=m)

        response = self.client.get(reverse('karty:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, m.name)
        self.assertNotContains(response, n.name)
        self.assertQuerysetEqual(response.context['page'],
                ['<MenuCard: menu 1>'])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_ordering_index_by_default(self):
        """
        Check that menucards are ordered by pk by default
        """
        m = MenuCardFactory(name='menu 3')
        n = MenuCardFactory(name='menu 2')
        o = MenuCardFactory(name='menu 1')
        for x in range(2):
            DishFactory(menucard=m)
        DishFactory(menucard=n)
        for x in range(3):
            DishFactory(menucard=o)

        response = self.client.get(reverse('karty:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['page'],
                ['<MenuCard: menu 3>', '<MenuCard: menu 2>',
                    '<MenuCard: menu 1>'])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_ordering_index_by_pk(self):
        """
        Check that menucards are ordered by pk when 'pk' is passed in query
        """
        m = MenuCardFactory(name='menu 3')
        n = MenuCardFactory(name='menu 2')
        o = MenuCardFactory(name='menu 1')
        for x in range(2):
            DishFactory(menucard=m)
        DishFactory(menucard=n)
        for x in range(3):
            DishFactory(menucard=o)

        response = self.client.get(reverse('karty:index') + '?ordering=pk')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['page'],
                ['<MenuCard: menu 3>', '<MenuCard: menu 2>',
                    '<MenuCard: menu 1>'])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_ordering_index_by_name(self):
        """
        Check that menucards are ordered by name when 'name' is passed in query
        """
        m = MenuCardFactory(name='menu 3')
        n = MenuCardFactory(name='menu 2')
        o = MenuCardFactory(name='menu 1')
        for x in range(2):
            DishFactory(menucard=m)
        DishFactory(menucard=n)
        for x in range(3):
            DishFactory(menucard=o)

        response = self.client.get(reverse('karty:index') + '?ordering=name')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['page'],
                ['<MenuCard: menu 1>', '<MenuCard: menu 2>',
                    '<MenuCard: menu 3>'])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_ordering_index_by_num_dishes(self):
        """
        Check that menucards are ordered by dish count when 'num_dishes'
        is passed in query
        """
        m = MenuCardFactory(name='menu 3')
        n = MenuCardFactory(name='menu 2')
        o = MenuCardFactory(name='menu 1')
        for x in range(2):
            DishFactory(menucard=m)
        DishFactory(menucard=n)
        for x in range(3):
            DishFactory(menucard=o)

        response = self.client.get(reverse('karty:index') + '?ordering=num_dishes')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['page'],
                ['<MenuCard: menu 2>', '<MenuCard: menu 3>',
                    '<MenuCard: menu 1>'])
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_pagination_first_page_many_menucards(self):
        """
        On first page with many menucards there should be:
        * no prev page link
        * next page link
        """
        for x in range(25):
            m = MenuCardFactory()
            DishFactory(menucard=m)

        response = self.client.get(reverse('karty:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '?page=2')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_pagination_page1_many_menucards(self):
        """
        Even if page=1, on first page with many menucards there should be:
        * no prev page link
        * next page link
        """
        for x in range(25):
            m = MenuCardFactory()
            DishFactory(menucard=m)

        response = self.client.get(reverse('karty:index') + '?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['prev_qstring'], '')
        self.assertEqual(response.context['next_qstring'], '?page=2')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_pagination_second_page_many_menucards(self):
        """
        On second page with many menucards there should be:
        * previous page link
        * next page link
        """
        for x in range(25):
            m = MenuCardFactory()
            DishFactory(menucard=m)

        response = self.client.get(reverse('karty:index') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['prev_qstring'], '?page=1')
        self.assertEqual(response.context['next_qstring'], '?page=3')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_pagination_last_page_many_menucards(self):
        """
        On last page with many menucards there should be:
        * previous page link
        * no next page link
        """
        for x in range(25):
            m = MenuCardFactory()
            DishFactory(menucard=m)

        response = self.client.get(reverse('karty:index') + '?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['prev_qstring'], '?page=2')
        self.assertEqual(response.context['next_qstring'], '')


class MenuCardDetailTests(TestCase):
    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_index_view_with_no_menucards(self):
        m = MenuCardFactory()
        for x in range(5):
            DishFactory(menucard=m)

        response = client.get(m.get_absolute_url())

        self.assertEqual(response.status_code, 200)
