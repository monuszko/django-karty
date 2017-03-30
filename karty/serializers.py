from rest_framework import serializers

from .models import MenuCard, Dish


class MenuCardSerializer(serializers.ModelSerializer):
    dishes = serializers.PrimaryKeyRelatedField(
            many=True,
            read_only=True,
            )
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    num_dishes = serializers.IntegerField(
            source='dishes.count',
            read_only=True
    )
    pub_date = serializers.DateTimeField(format='%d %b %Y')
    mod_date = serializers.DateTimeField(format='%d %b %Y')

    class Meta:
        model = MenuCard
        fields = ('name', 'desc', 'pub_date', 'mod_date', 'url', 'dishes',
                'num_dishes')

