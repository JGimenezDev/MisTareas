# forms.py
from django import forms
from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'fecha', 'descripcion', 'prioridad', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ir al cine...'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Pasar por Juan y Micaela...'}),
            'prioridad': forms.RadioSelect(),
            'categoria': forms.Select(attrs={'class': 'form-control'})
        }