from django.db import models

class TiposAtributos(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    descripcion = models.CharField(max_length=100, blank=True, default='')
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codigo + "-" + self.descripcion

    class Meta:
        ordering = ('codigo',)
