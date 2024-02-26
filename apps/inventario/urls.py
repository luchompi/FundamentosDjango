from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.saludo),
    path('listar/', views.mostrar_ingredientes),
    path('crear/', views.crear_ingrediente),
    path('editar/', views.actualizar_ingrediente),
    path('eliminar/', views.eliminar_ingrediente),

    #API
    path('',views.IngredientesController.as_view()),
]
