# en principal/views.py
from django.shortcuts import render

def pagina_principal(request):
    context = {'titulo_pagina': 'Inicio','contenido_pagina':'Esto es lo que se vería dentro de la página de inicio'}
    return render(request, 'principal/pagina.html', context)

def pagina_contacto(request):
    context = {'titulo_pagina': 'Contacto','contenido_pagina':'Esto es lo que se vería en la página de contacto: formularios, botones, etc.'}
    return render(request, 'principal/pagina.html', context)