from rest_framework import serializers
from . models import House, photo


class photoserializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = ['photo', 'house']


class houseserializer(serializers.ModelSerializer):
    photos = photoserializer(read_only=True, many=True)

    class Meta:
        model = House
        fields = [
            'id',
            'owner',
            'price',
            'location',
            'area',
            'address',
            'description',
            'public',
            'bed_rooms',
            'bath_rooms',
            'living_rooms',
            'photos',
        ]
    
    
