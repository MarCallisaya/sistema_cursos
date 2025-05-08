from django.urls import path
from .views import dasboard

urlpatterns = [
    path('', dasboard,name='dashboard'),
]
