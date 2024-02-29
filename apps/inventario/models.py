from django.db import models

# Create your models here.

"""
Django shell
1. python manage.py shell
2. from django.db import connection
3. from apps.inventario.models import Ingredientes
4.
"""


class Ingredientes(models.Model):
    # Queremos que el nombre de un ingrediente sea unico
    # Es decir, no puedene haber dos ingredientes con el mismo nombre.
    nombre = models.CharField(max_length=100, unique=True, error_messages={
                              'unique': 'el registro ya existe!!'})  # nombre
    cantidad = models.IntegerField(default=1)  # cantidad
    fecha_regitro = models.DateField(
        auto_now_add=True, null=True, blank=True)
    hora_registro = models.TimeField(auto_now_add=True, null=True, blank=True)
    # variable = model.tipoDato(opciones, valor_predetermiado, mensaje_error,
    # valor_max,valor_min ... primary_key, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Recetas(models.Model):
    nombre = models.CharField(max_length=150, unique=True, error_messages={
        'unique': 'La receta ya fue creada'
    })
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre
