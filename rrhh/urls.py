from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),

    # Empleados
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='empleado_crear'),
    path('empleados/editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),

    # Departamentos
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('departamentos/crear/', views.crear_departamento, name='crear_departamento'),
    path('departamentos/editar/<int:id>/', views.editar_departamento, name='editar_departamento'),
    path('departamentos/eliminar/<int:id>/', views.eliminar_departamento, name='eliminar_departamento'),

    # Cargos
    path('cargos/', views.lista_cargos, name='lista_cargos'),
    path('cargos/crear/', views.crear_cargo, name='crear_cargo'),
    path('cargos/editar/<int:id>/', views.editar_cargo, name='editar_cargo'),
    path('cargos/eliminar/<int:id>/', views.eliminar_cargo, name='eliminar_cargo'),

    # Contratos
    path('contratos/', views.lista_contratos, name='lista_contratos'),
    path('contratos/crear/', views.crear_contrato, name='crear_contrato'),
    path('contratos/editar/<int:id>/', views.editar_contrato, name='editar_contrato'),
    path('contratos/eliminar/<int:id>/', views.eliminar_contrato, name='eliminar_contrato'),

]
=======
    path('', views.home, name='home'),

    path(
        'empleados/',
        views.lista_empleados,
        name='lista_empleados'
    ),

    path(
        'empleados/crear/',
        views.crear_empleado,
        name='crear_empleado'
    ),

    path(
        'empleados/<int:pk>/editar/',
        views.editar_empleado,
        name='empleado_editar'
    ),

    path(
        'departamentos/',
        views.lista_departamentos,
        name='lista_departamentos'
    ),

    path(
        'departamentos/crear/',
        views.crear_departamento,
        name='crear_departamento'
    ),
]
>>>>>>> Stashed changes
