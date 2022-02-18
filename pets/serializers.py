from rest_framework import serializers

from .models import (
    Pet,
    Breed,
    Health,
    Address,
    Classification
)


class PetSerializer(serializers.ModelSerializer):
    health = serializers.SerializerMethodField()
    classification = serializers.SerializerMethodField()
    bread = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ('id', 'name', 'birthday', 'photo',
                  'description', 'is_home', 'classification', 'health', 'bread', 'address')
        swagger_schema_fields = {
            'description': 'Model pet',
        }

    def get_health(self, obj: Pet) -> str:
        return obj.health.name

    def get_classification(self, obj: Pet) -> str:
        return obj.classification.name

    def get_bread(self, obj: Pet) -> str:
        return obj.bread.name

    def get_address(self, obj: Pet) -> str:
        return obj.address.city


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name', 'description')
        swagger_schema_fields = {
            'description': 'Pet breed',
        }


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ('id', 'name', 'description')
        swagger_schema_fields = {
            'description': 'Pet health status',
        }


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'city', 'street', 'house_number', 'description')
        swagger_schema_fields = {
            'description': 'Address where the pet is located',
        }


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ('id', 'name', 'description')
        swagger_schema_fields = {
            'description': 'Pet classification',
        }
