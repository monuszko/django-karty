from django.test import Client, TestCase
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


client = Client()


class MenuCardListTests(TestCase):
    def test_index_view_with_no_menucards(self):
        """
        If no menucards exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('karty:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _("No menu cards are available"))
        self.assertQuerysetEqual(response.context['page'], [])
