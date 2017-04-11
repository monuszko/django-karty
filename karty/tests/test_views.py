from django.test import Client, TestCase, override_settings
from django.urls import reverse


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
