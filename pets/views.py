from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PetSerializer
from .models import (
    Pet,
    Breed,
    Health,
    Address,
    Classification
)


class PetView(ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class SinglePetView(RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
