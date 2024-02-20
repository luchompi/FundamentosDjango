from django.db import models

# Create your models here.


class Ingredientes(models.Model):
    nombre = models.CharField(max_length=100)  # nombre
    cantidad = models.IntegerField(default=1)  # cantidad
    fecha_regitro = models.DateField(
        auto_now_add=True, null=True, blank=True)
    hora_registro = models.TimeField(auto_now_add=True, null=True, blank=True)
    # variable = model.tipoDato(opciones, valor_predetermiado, mensaje_error,
    # valor_max,valor_min ... primary_key, unique=True, null=True, blank=True)
    def __str__(self):
        return self.nombre