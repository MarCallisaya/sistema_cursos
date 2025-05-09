from django.urls import path
from .views import dashboard,dashboard_admin,dashboard_docente

urlpatterns = [
    path('', dashboard,name='dashboard'),
    path('admin-dashboard/',dashboard_admin, name='dashboard_admin'),
    path('docente-dashboard/',dashboard_admin, name='dashboard_docente'),
    path('estudiante-dashboard/',dashboard_admin, name='dashboard_estudiante'),
]
