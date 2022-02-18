from django.urls import path, include

from .views import (
    UserView,
    SingleUserView,
    ShelterView,
    SingleShelterView
)

urlpatterns = [
    path('users/', include([
        path('', UserView.as_view()),
        path('<int:pk>/', SingleUserView.as_view())
    ])),
    path('shelters/', include([
        path('', ShelterView.as_view()),
        path('<int:pk>/', SingleShelterView.as_view())
    ])),
]
