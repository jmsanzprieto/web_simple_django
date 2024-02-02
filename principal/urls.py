# en principal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('contacto/', views.pagina_contacto, name='pagina_contacto'),
]
