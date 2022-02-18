from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import UserSerializer, ShelterSerializer

from .models import User, Shelter


class UserView(ListCreateAPIView):
    """Unload and create for a user model"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SingleUserView(RetrieveUpdateDestroyAPIView):
    """Updating and deleting for the selected user model entry"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShelterView(ListCreateAPIView):
    """Unload and create for a shelter model"""

    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer


class SingleShelterView(RetrieveUpdateDestroyAPIView):
    """Updating and deleting for the selected shelter model entry"""
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
