# en principal/urls.py
from django.urls import path
from .views import mostrar_pagina

urlpatterns = [
    path('<str:nombre_pagina>/', mostrar_pagina, name='mostrar_pagina'),
]
