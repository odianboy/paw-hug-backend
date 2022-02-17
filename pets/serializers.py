from rest_framework import serializers

from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'birthday', 'photo',
                  'description', 'is_home', 'classification', 'health', 'bread', 'address')
