from django.contrib import admin
from .models import (Categoria, Tarea)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria']

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'fecha']
    list_filter = ['prioridad', 'categoria']
    search_fields = ['descripcion']