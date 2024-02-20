from django.http import HttpResponse
from django.shortcuts import render
from .models import Ingredientes
# Create your views here.


def saludo(request):
    """
    q es quien recibe los datos de la consulta
    Ingredientes es la tabla
    objects es quien hace la consulta
    all() es quien trae todos los datos
    Select * from Ingredientes
    Select es object 
    * es all
    Ingredientes es la tabla
    """
    # q = Ingredientes.objects.all()
    """Ingrediente con la id 3
    Select * from Ingredientes where id = 3
    """
    # q = Ingredientes.objects.get(id=3)
    # get solo retorna un valor

    """ingredientes cuya cantidad sea mayor o igual a 10
    Select * from Ingredientes where cantidad > 10
    """
    # q = Ingredientes.objects.filter(cantidad__gte=10)
    # gte significa greater than or equal
    # q = Ingredientes.objects.filter(cantidad__lte=10)
    # lte significa less than or equal
    q = Ingredientes.objects.filter(cantidad__lte=10, nombre__contains="i")
    # Filter retorna uno o más
    # Ingredientes.objects.first() retorna el primer registro
    # Ingredientes.objects.last() retorna el último registro
    # Ingredientes.objects.order_by("-nombre") ordena los registros por nombre
    # get_object_or_404(Ingredientes, id=3) retorna el registro con id 3
    # get_list_or_404(Ingredientes, cantidad__gte=10) retorna los registros con cantidad mayor o igual a 10
    # F y Q, son para hacer consultas más complejas, and , or.... 
    print(q)

    return HttpResponse("Luis")


"""
1. escribes una url (www.misito.com/inventairo)
2. Django evalua esa url
3. si la url es correcta, entonces ejecuta la funcion saludo
"""
