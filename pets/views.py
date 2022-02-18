from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import (
    PetSerializer,
    BreedSerializer,
    HealthSerializer,
    AddressSerializer,
    ClassificationSerializer
)

from .models import (
    Pet,
    Breed,
    Health,
    Address,
    Classification
)


class PetView(ListCreateAPIView):
    """Unload and create for a pet Model"""

    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class SinglePetView(RetrieveUpdateDestroyAPIView):
    """Updating and deleting for the selected pet model entry"""
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class BreedView(ListCreateAPIView):
    """Unload and create for a breed Model"""
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class SingleBreedView(RetrieveUpdateDestroyAPIView):
    """Updating and deleting for the selected breed model entry"""
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class HealthView(ListCreateAPIView):
    """Unload and create for a health Model"""
    queryset = Health.objects.all()
    serializer_class = HealthSerializer


class SingleHealthView(RetrieveUpdateDestroyAPIView):
    """Updating and deleting for the selected health model entry"""
    queryset = Health.objects.all()
    serializer_class = HealthSerializer


class AddressView(ListCreateAPIView):
    """Unload and create for a address Model"""
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class SingleAddressView(RetrieveUpdateDestroyAPIView):
    """Updating and deleting for the selected address model entry"""
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class ClassificationView(ListCreateAPIView):
    """Unload and create for a classification Model"""
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class SingleClassificationView(RetrieveUpdateDestroyAPIView):
    """Updating and deleting for the selected classification model entry"""
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
