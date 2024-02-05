# en principal/views.py
from django.shortcuts import render

def mostrar_pagina(request, nombre_pagina):
    contenido = obtener_contenido(nombre_pagina)
    context = {'titulo_pagina': nombre_pagina.capitalize(), 'contenido_pagina': contenido}
    return render(request, 'principal/pagina.html', context)

def obtener_contenido(nombre_pagina):
    # Puedes agregar más páginas y su contenido aquí según sea necesario
    paginas = {
        'inicio': 'Esto es lo que se vería dentro de la página de inicio',
        'contacto': 'Esto es lo que se vería en la página de contacto: formularios, botones, etc.',
        # Agrega más páginas según sea necesario
    }

    # Devuelve el contenido de la página correspondiente o un mensaje de error si no existe
    return paginas.get(nombre_pagina, 'Error 404: Página no encontrada')
