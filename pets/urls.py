from django.urls import path, include

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
    path('pets/', include([
        path('', PetView.as_view()),
        path('<uuid:pk>/', SinglePetView.as_view())
    ])),
    path('breeds/', include([
        path('', BreedView.as_view()),
        path('<int:pk>/', SingleBreedView.as_view()),
    ])),
    path('healths/', include([
        path('', HealthView.as_view()),
        path('<int:pk>/', SingleHealthView.as_view()),
    ])),
    path('address/', include([
        path('', AddressView.as_view()),
        path('<int:pk>/', SingleAddressView.as_view()),
    ])),
    path('classification/', include([
        path('', ClassificationView.as_view()),
        path('classification/<int:pk>', SingleClassificationView.as_view())
    ])),
]
