from django.urls import path

from .views import (
    PetView,
    SinglePetView,
    BreedView,
    SingleBreedView,
    HealthView,
    SingleHealthView,
    AddressView,
    SingleAddressView,
    ClassificationView,
    SingleClassificationView
)

urlpatterns = [
    path('pets/', PetView.as_view()),
    path('pets/<uuid:pk>', SinglePetView.as_view()),
    path('breeds/', BreedView.as_view()),
    path('breeds/<int:pk>', SingleBreedView.as_view()),
    path('healths/', HealthView.as_view()),
    path('healths/<int:pk>', SingleHealthView.as_view()),
    path('address/', AddressView.as_view()),
    path('address/<int:pk>', SingleAddressView.as_view()),
    path('classification/', ClassificationView.as_view()),
    path('classification/<int:pk>', SingleClassificationView.as_view()),
]
