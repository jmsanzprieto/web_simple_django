from django.shortcuts import render, get_object_or_404
from .models import Pagina
from django.http import HttpResponseRedirect
from django.urls import reverse

def mostrar_pagina(request, nombre_pagina):
    # Convertir nombre_pagina a minúsculas
    nombre_pagina = nombre_pagina.lower()

    try:
        # Intentar obtener una instancia de Pagina
        pagina = get_object_or_404(Pagina, nombre=nombre_pagina)

        # Crear un contexto con el nombre de la página y el contenido de la página
        context = {'titulo_pagina': pagina.nombre.capitalize(), 'contenido_pagina': pagina.contenido}

        # Renderizar la plantilla 'pagina.html' con el contexto proporcionado
        return render(request, 'principal/pagina.html', context)
    except:
        # Si no se encuentra la página, redirigir a la página con nombre "error"
        return HttpResponseRedirect(reverse('mostrar_pagina', args=['error']))

