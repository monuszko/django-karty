import datetime
import factory
import random

from faker import Faker

from .models import MenuCard, Dish

fake = Faker()


class MenuCardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MenuCard
    
    desc = factory.Faker('sentence', nb_words=5, variable_nb_words=True)

    @factory.sequence
    def name(n):
        return 'Menu %s %d' % (' '.join(fake.words(nb=5)), n)

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        pub_date = kwargs.pop('pub_date', None)
        mod_date = kwargs.pop('mod_date', None)
        obj = super(MenuCardFactory, cls)._create(target_class, *args, **kwargs)
        if pub_date is not None:
            obj.pub_date = pub_date
        if mod_date is not None:
            obj.mod_date = mod_date
        obj.save()
        return obj


class DishFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dish

    menucard = factory.SubFactory(MenuCardFactory)
    price = factory.Faker('pydecimal',
            left_digits=2, right_digits=2, positive=True)
    time = datetime.timedelta(minutes=60) * random.random()

    desc = factory.Faker('sentence', nb_words=5, variable_nb_words=True)
    vege = factory.Faker('boolean', chance_of_getting_true=30)

    @factory.sequence
    def name(n):
        return '%s' % ' '.join(fake.words(nb=5))
