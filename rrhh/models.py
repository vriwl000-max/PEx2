from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models


class Usuario(AbstractUser):
    cedula = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.TextField(blank=True)

    class Meta:
        db_table = 'usuario'


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self): return self.nombre


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self): return self.nombre


class Empleado(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    fecha_ingreso = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"


class Contrato(models.Model):
    TIPOS_CONTRATO = [
        ('INDEFINIDO', 'Indefinido'),
        ('PLAZO_FIJO', 'Plazo Fijo'),
        ('PRUEBA', 'Período de Prueba'),
        ('OCASIONAL', 'Ocasional'),
    ]
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, limit_choices_to={'activo': True})
    tipo_contrato = models.CharField(max_length=20, choices=TIPOS_CONTRATO)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('400.00'), message="El salario debe ser mayor a cero.")])
    estado = models.BooleanField(default=True)  # Eliminado lógico

    def __str__(self):
        return f"Contrato {self.tipo_contrato} - {self.empleado}"


class Asistencia(models.Model):
    ESTADOS_ASISTENCIA = [
        ('PRESENTE', 'Presente'),
        ('ATRASO', 'Atraso'),
        ('FALTA', 'Falta Injustificada'),
        ('PERMISO', 'Permiso Médico / Justificado'),
    ]
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, limit_choices_to={'activo': True})
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(null=True, blank=True)
    observacion = models.CharField(max_length=200, blank=True)
    tipo_asistencia = models.CharField(max_length=20, choices=ESTADOS_ASISTENCIA, default='PRESENTE')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.empleado} - {self.fecha} ({self.tipo_asistencia})"