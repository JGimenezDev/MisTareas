from django.db import models
from django.utils import timezone
from .managers import TareasManager

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.categoria}'
    
    
class Tarea(models.Model):
    
    PRIO = (
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
    )
    
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True)
    prioridad = models.CharField(max_length=1, choices=PRIO, default='0')
    fecha = models.DateField()
    agregada = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria,
                                  on_delete=models.CASCADE,
                                  related_name='tareas',
                                  blank=True,
                                  null=True)
    completa = models.BooleanField(default=False)
    
    objects = TareasManager()
    
    def __str__(self):
        return f'{self.titulo}'
    
    def save(self, *args, **kwargs):
        # Verificar si la tarea está completada basándose en la fecha
        if self.fecha < timezone.now().date():
            self.completa = True
        super().save(*args, **kwargs)