from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Empleado, Departamento, Cargo, Contrato, Asistencia, Usuario

################################
#USUARIO
#############################
class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'cedula', 'telefono', 'fecha_nacimiento', 'direccion']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula', '')
        if not cedula.isdigit() or len(cedula) != 10:
            raise ValidationError("La cédula debe contener exactamente 10 dígitos numéricos.")
        return cedula
    
############################
#eMPLEADO
##############################

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        exclude = ['activo', 'fecha_ingreso']
        fields = ['usuario', 'departamento', 'cargo', 'activo']

#################################
#DEPARTAMENTO
#############################

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        exclude = ['estado']
        fields = ['nombre']

#############################
#CARGO
#############################

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        exclude = ['estado']
        fields = ['nombre']

###########################
#CONTRATO
###########################

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        exclude = ['estado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        datos = super().clean()
        inicio = datos.get('fecha_inicio')
        fin = datos.get('fecha_fin')

        if inicio and fin and fin < inicio:
            raise ValidationError("La fecha de finalización no puede ser anterior a la de inicio.")
        return datos

############################
#ASISTENCIA
###########################

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        exclude = ['estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_entrada': forms.TimeInput(attrs={'type': 'time'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        datos = super().clean()
        entrada = datos.get('hora_entrada')
        salida = datos.get('hora_salida')
        empleado = datos.get('empleado')
        fecha = datos.get('fecha')

        if entrada and salida and salida <= entrada:
            raise ValidationError("La hora de salida debe ser posterior a la hora de entrada.")

        if not self.instance.pk and Asistencia.objects.filter(empleado=empleado, fecha=fecha, estado=True).exists():
            raise ValidationError("Registro duplicado: ya existe asistencia para este empleado en esa fecha.")
        return datos
