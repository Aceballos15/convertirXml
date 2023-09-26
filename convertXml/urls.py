from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrincipalView

from django.urls import path
from . import views

urlpatterns = [
    path('', PrincipalView.as_view(), name='convertir'),
]