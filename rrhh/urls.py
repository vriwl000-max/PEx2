from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='empleado_crear'),
    path('empleados/<int:pk>/editar/', views.editar_empleado, name='empleado_editar'),
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('departamentos/crear/', views.crear_departamento, name='crear_departamento'),
]
