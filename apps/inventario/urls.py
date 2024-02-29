from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('hola/', views.saludo),
    path('listar/', views.mostrar_ingredientes),
    path('crear/', views.crear_ingrediente),
    path('editar/', views.actualizar_ingrediente),
    path('eliminar/', views.eliminar_ingrediente),

    # API
    path('', views.IngredientesController.as_view()),
    path('ingrediente/<int:id>/', views.DetalleIngredienteCotroller.as_view()),
    # localhost:8000/inventario/ingrediente/3000/
    path('recetas/',views.RecetasController.as_view()),
    path('recetas/<int:id>/',views.DetalleRecetaController.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
