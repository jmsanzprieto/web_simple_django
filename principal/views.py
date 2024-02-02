# en principal/views.py

from django.shortcuts import render

## Metodo para llamar a la página principal
def pagina_principal(request):
    return render(request, 'principal/pagina_principal.html')

## Metodo para llamar a la página de contacto
def pagina_contacto(request):
    return render(request, 'principal/pagina_contacto.html')

