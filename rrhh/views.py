from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Empleado, Departamento, Cargo, Contrato, Asistencia
from .forms import EmpleadoForm, DepartamentoForm, CargoForm, ContratoForm, AsistenciaForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_view(request):

    form = AuthenticationForm(
        request,
        data=request.POST or None
    )

    if request.method == 'POST':

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')

    return render(
        request,
        'principal/login.html',
        {'form': form}
    )

def home(request):
    return render(request, 'home.html')

#############################
#EMPLEADO VIEWS
#############################

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista.html', {'empleados': empleados})

def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_empleados')
    return render(request, 'empleados/crear.html', {'form': form})

#################################
#DEPARTAMENTO VIEWS
#################################

def lista_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/lista.html', {'departamentos': departamentos})

def crear_departamento(request):
    form = DepartamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_departamentos')
    return render(request, 'departamentos/crear.html', {'form': form})

####################################
#CARGO VIEWS
################################

@login_required(login_url='login')
def lista_cargos(request):
    cargos = Cargo.objects.filter(estado=True)
    return render(request, 'cargos/listar.html', {'cargos': cargos})

#############################
#CONTRATO VIEWS
#############################

@login_required(login_url='login')
def lista_contratos(request):
    contratos = Contrato.objects.filter(estado=True)
    return render(request, 'contratos/lista.html', {'contratos': contratos})

##############################
#ASISTENCIA VIEWS
##############################

@login_required(login_url='login')
def lista_asistencias(request):
    asistencias = Asistencia.objects.filter(estado=True)
    return render(request, 'asistencias/lista.html', {'asistencias': asistencias})

def editar_empleado(request, pk):
    return render(
        request,
        'empleados/editar.html'
    )