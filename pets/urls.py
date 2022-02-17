from django.urls import path

from .views import PetView, SinglePetView

urlpatterns = [
    path('pets/', PetView.as_view()),
    path('pets/<uuid:pk>', SinglePetView.as_view()),
]
