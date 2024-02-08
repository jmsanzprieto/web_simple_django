from django.urls import path
from .views import mostrar_pagina

urlpatterns = [
    # El parámetro nombre_pagina es ahora opcional
    path('<str:nombre_pagina>/', mostrar_pagina, name='mostrar_pagina'),
    path('', mostrar_pagina, {'nombre_pagina': 'inicio'}, name='mostrar_pagina_inicio'),  # Ruta para el caso vacío
]
