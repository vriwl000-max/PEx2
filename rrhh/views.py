from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Departamento, Cargo
from .forms import EmpleadoForm, DepartamentoForm, CargoForm

def home(request):
    return render(request, 'home.html')

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista.html', {'empleados': empleados})

def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_empleados')
    return render(request, 'empleados/crear.html', {'form': form})

def lista_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/lista.html', {'departamentos': departamentos})

def crear_departamento(request):
    form = DepartamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_departamentos')
    return render(request, 'departamentos/crear.html', {'form': form})