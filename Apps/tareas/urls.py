from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tareas_app'

urlpatterns = [
    # ------------------------ Urls para tareas -----------------------------------------------
    path("lista-tareas/", views.ListaTareas.as_view(), name = 'lista_tareas'),
    path("detalle-tarea/<pk>/", views.DetalleTarea.as_view(), name = 'detalle_tarea'),
    path("nueva-tarea", views.NuevaTarea.as_view(), name = 'nueva_tarea'),
    path("editar-tarea/<pk>/", views.EditarTarea.as_view(), name = 'editar_tarea'),
    path("eliminar-tarea/<pk>/", views.EliminarTarea.as_view(), name = 'eliminar_tarea'),
    
    
    # ------------------------ Urls para home -----------------------------------------------
    path("", views.HomeTareas.as_view(), name = 'home'),
]
