from django import forms
from .models import Empleado, Departamento, Cargo

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['usuario', 'departamento', 'cargo', 'activo']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre']

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre']

