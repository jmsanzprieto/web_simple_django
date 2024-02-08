from django.db import models

class Pagina(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    contenido = models.TextField()

    def __str__(self):
        return self.nombre
