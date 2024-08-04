from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView)
from .forms import TareaForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q

from .models import (Categoria, Tarea)


# ------------------------------------------- vista para las tareas --------------------

# vista que lista todas las tareas
class ListaTareas(ListView):
    template_name = 'tareas/lista_tareas.html'
    model = Tarea
    context_object_name = 'tareas'
    paginate_by = 7
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context
    
    
    def get_queryset(self):
        buscar = self.request.GET.get('buscar', '')
        orden = self.request.GET.get('orden', '')
        categoria = self.request.GET.get('cate', '')
        fecha1 = self.request.GET.get('fechaInicio', '')
        fecha2 = self.request.GET.get('fechaFin', '')
        
        if buscar:
            return Tarea.objects.Buscar(buscar)
        
        if categoria and fecha1 and fecha2:
            return Tarea.objects.Filtrar_todo(categoria, fecha1, fecha2)
        
        if fecha1 and fecha2:
            return Tarea.objects.Filtrar_por_fechas(fecha1, fecha2)
        
        if categoria:
            return Tarea.objects.Filtrar_por_categoria(categoria)
        
        return Tarea.objects.all()
    

# vista que muestra el detalle de una tarea
class DetalleTarea(DetailView):
    model = Tarea
    template_name = "tareas/detalle_tarea.html"
    context_object_name = 'tarea'
    
    
# vista para agregar una nueva tarea
class NuevaTarea(CreateView):
    template_name = "tareas/nueva_tarea.html"
    form_class = TareaForm
    success_url = reverse_lazy('tareas_app:lista_tareas')


# vista para editar una tarea
class EditarTarea(UpdateView):
    model = Tarea
    template_name = "tareas/editar_tarea.html"
    form_class = TareaForm
    success_url = reverse_lazy('tareas_app:lista_tareas')
    
    
# vista para eliminar una tarea 
class EliminarTarea(DeleteView):
    model = Tarea
    template_name = "tareas/eliminar_tarea.html"
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas_app:lista_tareas')


# ------------------------------------------- vista Home --------------------

class HomeTareas(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().date()
        
        #Devolver las ultimas 3 tareas agregadas...
        ultimas_tareas = Tarea.objects.all().filter(
            Q(fecha__gte = hoy)    
        ).order_by('fecha')[:3]
        
        #Devolver tareas completadas
        completadas = Tarea.objects.filter(
            #filtrar por fechas menor a la fecha actual
            fecha__lt = hoy
        ).order_by('-fecha')
        
        context['ultimas_tareas'] = ultimas_tareas
        context['completadas'] = completadas
        
        return context
    
