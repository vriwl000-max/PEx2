from django.contrib import admin
from .models import Usuario, Departamento, Cargo, Empleado, Contrato

admin.site.register(Usuario)
admin.site.register(Departamento)
admin.site.register(Cargo)
admin.site.register(Empleado)
admin.site.register(Contrato)