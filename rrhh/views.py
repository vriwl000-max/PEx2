from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Empleado, Departamento, Cargo, Contrato, Asistencia
from .forms import RegistroUsuarioForm, EmpleadoForm, DepartamentoForm, CargoForm, ContratoForm, AsistenciaForm
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
        messages.success(request, "Registro creado correctamente.")
        return redirect('lista_empleados')
    if request.method == 'POST':
        messages.error(request, "Error en el formulario.")
    return render(request, 'empleados/crear.html', {'form': form})

def editar_empleado(request, id):
    empleado = Empleado.objects.filter(id=id, activo=True).first()
    if not empleado:
        messages.error(request, "Registro no encontrado.")
        return redirect('lista_empleados')

    form = EmpleadoForm(request.POST or None, instance=empleado)
    if form.is_valid():
        form.save()
        messages.success(request, "Registro actualizado correctamente.")
        return redirect('lista_empleados')
    if request.method == 'POST':
        messages.error(request, "Error en el formulario.")
    return render(request, 'empleados/editar.html', {'form': form, 'modulo': 'empleados'})

@login_required(login_url='login')
def eliminar_empleado(request, id):
    empleado = Empleado.objects.filter(id=id, activo=True).first()
    if not empleado:
        messages.error(request, "Registro no encontrado.")
    else:
        empleado.activo = False
        empleado.save()
        messages.success(request, "Registro eliminado correctamente.")
    return redirect('lista_empleados')

#################################
#DEPARTAMENTO VIEWS
#################################

def lista_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/crear.html', {'departamentos': departamentos})

def crear_departamento(request):
    form = DepartamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_departamentos')
    return render(request, 'departamentos/crear.html', {'form': form})

def editar_departamento(request, pk):
    departamento = Departamento.objects.filter(pk=pk, estado=True).first()
    if not departamento:
        messages.error(request, "Registro no encontrado.")
        return redirect('lista_departamentos')

    form = DepartamentoForm(request.POST or None, instance=departamento)
    if form.is_valid():
        form.save()
        messages.success(request, "Registro actualizado correctamente.")
        return redirect('lista_departamentos')
    if request.method == 'POST':
        messages.error(request, "Error en el formulario.")
    return render(request, 'departamentos/editar.html', {'form': form, 'modulo': 'departamentos'})

@login_required(login_url='login')
def eliminar_departamento(request, pk):
    departamento = Departamento.objects.filter(pk=pk, estado=True).first()
    if not departamento:
        messages.error(request, "Registro no encontrado.")
        return redirect('lista_departamentos')

    departamento.estado = False
    departamento.save()
    messages.success(request, "Registro eliminado correctamente.")
    return redirect('lista_departamentos')
####################################
#CARGO VIEWS
################################

def lista_cargos(request):
    cargos = Cargo.objects.filter(estado=True)
    return render(request, 'cargos/listar.html', {'cargos': cargos})

@login_required(login_url='login')
def crear_cargo(request):
    form = CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registro creado correctamente.")
        return redirect('lista_cargos')
    if request.method == 'POST':
        messages.error(request, "Error en el formulario.")
    return render(request, 'cargos/crear.html', {'form': form, 'modulo': 'cargos'})


@login_required(login_url='login')
def editar_cargo(request, id):
    cargo = Cargo.objects.filter(id=id, estado=True).first()
    if not cargo:
        messages.error(request, "Registro no encontrado.")
        return redirect('lista_cargos')

    form = CargoForm(request.POST or None, instance=cargo)
    if form.is_valid():
        form.save()
        messages.success(request, "Registro actualizado correctamente.")
        return redirect('lista_cargos')
    if request.method == 'POST':
        messages.error(request, "Error en el formulario.")
    return render(request, 'cargos/editar.html', {'form': form, 'modulo': 'cargos'})


@login_required(login_url='login')
def eliminar_cargo(request, id):
    cargo = Cargo.objects.filter(id=id, estado=True).first()
    if not cargo:
        messages.error(request, "Registro no encontrado.")
        return redirect('lista_cargos')

    if request.method == 'POST':
        cargo.estado = False
        cargo.save()
        messages.success(request, "Registro eliminado correctamente.")
        return redirect('lista_cargos')

    return render(request, 'cargos/eliminar.html', {'cargo': cargo, 'modulo': 'cargos'})

#############################
#CONTRATO VIEWS
#############################

@login_required(login_url='login')
def lista_contratos(request):
    contratos = Contrato.objects.filter(estado=True)
    return render(request, 'contratos/crear.html', {'contratos': contratos})

@login_required(login_url='login')
def crear_contrato(request):
    form = ContratoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registro creado correctamente.")
        return redirect('lista_contratos')
    if request.method == 'POST':
        messages.error(request, "Error en el formulario.")
    return render(request, 'contratos/crear.html', {'form': form, 'modulo': 'contratos'})


@login_required(login_url='login')
def editar_contrato(request, id):
    contrato = Contrato.objects.filter(id=id, estado=True).first()
    if not contrato:
        messages.error(request, "Registro no encontrado.")
        return redirect('lista_contratos')

    form = ContratoForm(request.POST or None, instance=contrato)
    if form.is_valid():
        form.save()
        messages.success(request, "Registro actualizado correctamente.")
        return redirect('lista_contratos')
    if request.method == 'POST':
        messages.error(request, "Error en el formulario.")
    return render(request, 'contratos/editar.html', {'form': form, 'modulo': 'contratos'})


@login_required(login_url='login')
def eliminar_contrato(request, id):
    contrato = Contrato.objects.filter(id=id, estado=True).first()
    if not contrato:
        messages.error(request, "Registro no encontrado.")
    else:
        contrato.estado = False
        contrato.save()
        messages.success(request, "Registro eliminado correctamente.")
    return redirect('lista_contratos')

##############################
#ASISTENCIA VIEWS
##############################

@login_required(login_url='login')
def lista_asistencias(request):
    asistencias = Asistencia.objects.filter(estado=True)
    return render(request, 'asistencia/listar.html', {'asistencias': asistencias, 'modulo': 'asistencias'})

@login_required(login_url='login')
def crear_asistencia(request):
    form = AsistenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registro creado correctamente.")
        return redirect('lista_asistencias')
    if request.method == 'POST':
        messages.error(request, "Error en el formulario.")
    return render(request, 'asistencia/crear.html', {'form': form, 'modulo': 'asistencias'})


@login_required(login_url='login')
def editar_asistencia(request, id):
    asistencia = Asistencia.objects.filter(id=id, estado=True).first()
    if not asistencia:
        messages.error(request, "Registro no encontrado.")
        return redirect('lista_asistencias')

    form = AsistenciaForm(request.POST or None, instance=asistencia)
    if form.is_valid():
        form.save()
        messages.success(request, "Registro actualizado correctamente.")
        return redirect('lista_asistencias')
    if request.method == 'POST':
        messages.error(request, "Error en el formulario.")
    return render(request, 'asistencia/editar.html', {'form': form, 'modulo': 'asistencias'})


@login_required(login_url='login')
def eliminar_asistencia(request, id):
    asistencia = Asistencia.objects.filter(id=id, estado=True).first()
    if not asistencia:
        messages.error(request, "Registro no encontrado.")
        return redirect('lista_asistencias')

    if request.method == 'POST':
        asistencia.estado = False
        asistencia.save()
        messages.success(request, "Registro eliminado correctamente.")
        return redirect('lista_asistencias')

    return render(request, 'asistencia/eliminar.html', {'asistencia': asistencia, 'modulo': 'asistencias'})
