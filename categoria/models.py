from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=100)
    observaciones = models.TextField()
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre