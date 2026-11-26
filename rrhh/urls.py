from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='empleado_crear'),
    #path('empleados/<int:pk>/editar/', views.editar_empleado, name='empleado_editar'),

    path('cargos/', views.lista_cargos, name='lista_cargos'),

    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('departamentos/crear/', views.crear_departamento, name='crear_departamento'),


    path('contratos/', views.lista_contratos, name='lista_contratos'),

    path('asistencias/', views.lista_asistencias, name='lista_asistencias'),
]
