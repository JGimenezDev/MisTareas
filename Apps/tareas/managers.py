from django.db import models
from django.db.models import Q
from django.utils import timezone


class TareasManager(models.Manager):
    
    def Buscar(self, clave):
        res = self.filter(
            Q(titulo__icontains = clave) |
            Q(descripcion__icontains = clave)
        ).exclude(
            fecha__lt = timezone.now().date()
        )
        return res
    
    def Filtrar_por_fechas(self, inicio, fin):
        res = self.filter(
            Q(fecha__gte = inicio),
            Q(fecha__lte = fin)
        ).order_by('fecha')
        return res
    
    def Filtrar_por_categoria(self, cate):
        res = self.filter(
            categoria = cate
        ).order_by('fecha')
        return res
    
    def Filtrar_todo(self, cate, f_inicio, f_fin):
        res = self.filter(
            Q(categoria = cate),
            Q(fecha__gte = f_inicio),
            Q(fecha__lte = f_fin)
        ).order_by('fecha')
        return res
    