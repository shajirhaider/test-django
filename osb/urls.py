
from django.urls import path, include
from .views import osb


urlpatterns = [
    path('osb/', osb),
]