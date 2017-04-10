from django.test import TestCase

from karty.serializers import MenuCardSerializer
from karty.factories import MenuCardFactory
from karty.models import MenuCard


class MenuCardSerializerTests(TestCase):
    def test_serializer_can_be_instantiated(self):
        for x in range(18):
            MenuCardFactory()

    menucards = MenuCard.objects.all()
    serializer = MenuCardSerializer(menucards, many=True)
            

