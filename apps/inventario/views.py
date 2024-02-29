from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
# from django.shortcuts import render
from apps.inventario.serializer import IngredientesSerializer,RecetasSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Ingredientes,Recetas
from django.shortcuts import get_object_or_404
# Create your views here.


"""
Procedimiento de consulta, es el proceso de obtener datos de una base de datos.
C.R.U.D.
C es crear registros - OK
R es leer registros - OK
U es actualizar registros - OK
D es eliminar registros - OK
"""


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
    # q = Ingredientes.objects.filter(cantidad__lte=10, nombre__contains="i")
    # Filter retorna uno o más
    # Ingredientes.objects.first() retorna el primer registro
    # Ingredientes.objects.last() retorna el último registro
    # Ingredientes.objects.order_by("-nombre") ordena los registros por nombre
    # get_object_or_404(Ingredientes, id=3) retorna el registro con id 3
    # get_list_or_404(Ingredientes, cantidad__gte=10) retorna los registros con cantidad mayor o igual a 10
    # F y Q, son para hacer consultas más complejas, and , or....
    # print(q)

    """Crear un registro
    ingrediente = Ingredientes(
        nombre="Perejil",
        cantidad=8
    )
    ingrediente.save()
    """

    """Eliminar un registro
    #1 consultar el registro en la base de datos
    ingrediente = Ingredientes.objects.get(id=6)
    #2 eliminar el registro
    ingrediente.delete()
    """

    """Actualizar un registro
    ingrediente = Ingredientes.objects.get(id=7)
    ingrediente.nombre = "Ajo"
    ingrediente.cantidad = 0
    ingrediente.save()
    """

    return HttpResponse("Luis")


def mostrar_ingredientes(request):
    ingredientes = Ingredientes.objects.all()
    print(ingredientes)
    return HttpResponse("Ingredientes")


def crear_ingrediente(request):
    ingrediente = Ingredientes(
        nombre="Pollo congelado",
        cantidad=22
    )
    ingrediente.save()
    return HttpResponse("Ingrediente creado")


def actualizar_ingrediente(request):
    ingrediente = Ingredientes.objects.get(id=9)
    ingrediente.cantidad = 40
    ingrediente.save()
    return HttpResponse("Actualizacion Completa!!!")


def eliminar_ingrediente(request):
    # ORM de django que se llama DjangoORM
    ingrediente = Ingredientes.objects.get(id=10)
    ingrediente.delete()
    return HttpResponse("Ingrediente eliminado")


"""
1. escribes una url (www.misito.com/inventairo)
2. Django evalua esa url
3. si la url es correcta, entonces ejecuta la funcion saludo
"""


class IngredientesController(APIView):
    def get(self, request):
        """Este medoto consulta los datos de la base de datos 
        y los retorna como json
        {
            [
                {"id":1, "nombre":"Perejil", "cantidad":10},
                {"id":2, "nombre":"Ajo", "cantidad":5},
                {"id":3, "nombre":"Cebolla", "cantidad":8}
            ]
        }
        """
        # REST se vale del ORM de django para hacer consultas
        ingredientes = Ingredientes.objects.all()
        serializer = IngredientesSerializer(ingredientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        La request es quien recibe los datos, el tipo de peticion y demás informacion
        data: {['nombre':'Perejil', 'cantidad':10]}

        """
        # Metodo HTTP
        # print(request.method)
        # data
        # print(request.data)
        data = request.data
        serializer = IngredientesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Se guardó el registro")
        return Response(serializer.errors)


class DetalleIngredienteCotroller(APIView):
    def get(self, request, id):
        ingrediente = get_object_or_404(Ingredientes, id=id)
        serializer = IngredientesSerializer(ingrediente)
        return Response(serializer.data)

    def put(self, request, id):
        ingrendiente = Ingredientes.objects.get(id=id)
        data = request.data
        serializer = IngredientesSerializer(
            ingrendiente, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Se ha actualizado el registro")
        return Response(serializer.errors)

    def delete(self, request, id):
        ingrediente = Ingredientes.objects.get(id=id)
        ingrediente.delete()
        return Response("Se ha eliminado el registro")
    
class RecetasController(APIView):
    def get(self,request):
        recetas = Recetas.objects.all()
        serializer = RecetasSerializer(recetas,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        datos = request.data
        serializer = RecetasSerializer(data=datos) 
        if serializer.is_valid():
            serializer.save()
            return Response("Se guardó el registro")
        return Response(serializer.errors)

class DetalleRecetaController(APIView):
    def get(self,request,id):
        receta = Recetas.objects.get(id=id)
        serializer = RecetasSerializer(receta)
        return Response(serializer.data)
    
    def put(self,request,id):
        receta = Recetas.objects.get(id=id)
        data = request.data
        serializer = RecetasSerializer(receta,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Se ha actualizado el registro")
        return Response(serializer.errors)
    
    def delete(self,request,id):
        receta = Recetas.objects.get(id=id)
        receta.delete()
        return Response("Se ha eliminado el registro")