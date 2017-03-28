from rest_framework import serializers

from .models import MenuCard 


class MenuCardSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    num_dishes = serializers.IntegerField(
            source='dish_set.count',
            read_only=True
    )
    pub_date = serializers.DateTimeField(format='%d %b %Y')
    mod_date = serializers.DateTimeField(format='%d %b %Y')

    class Meta:
        model = MenuCard
        fields = ('name', 'desc', 'pub_date', 'mod_date', 'url', 'num_dishes')

