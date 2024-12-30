from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("service/<int:id>/", service, name="service"),
]
