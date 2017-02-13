import factory

from datetime import timedelta

from .models import MenuCard, Dish


class MenuCardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MenuCard

    name = factory.Sequence(lambda n: "Card %d" % n)
    desc = factory.Sequence(lambda n: "Card description %d" % n)


class DishFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dish 

    menucard = factory.SubFactory(MenuCardFactory)
    price = factory.Sequence(lambda n: n % 25)
    time = timedelta(minutes=25)

    name = factory.Sequence(lambda n: "Dish %d" % n)
    desc = factory.Sequence(lambda n: "Dish description %d" % n)
