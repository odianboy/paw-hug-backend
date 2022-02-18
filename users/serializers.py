from rest_framework import serializers

from .models import (
    User,
    Shelter,
)


class UserSerializer(serializers.ModelSerializer):
    pet = serializers.SerializerMethodField()
    shelter = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'avatar',
                  'email', 'phone', 'pet', 'shelter', )
        swagger_schema_fields = {
            'description': 'Model user',
        }

    def get_pet(self, obj: User) -> str:
        return obj.pet.name

    def get_shelter(self, obj: User) -> str:
        return obj.shelter.name


class ShelterSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = Shelter
        fields = ('id', 'name', 'description', 'address',
                  'site', 'email', 'phone')
        swagger_schema_fields = {
            'description': 'Model shelter',
        }

    def get_address(self, obj: Shelter) -> str:
        return obj.address.city
