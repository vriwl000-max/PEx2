from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.db.models import Q

def empleado_listar(request):
    buscar = request.GET.get('buscar', '')
    empleados = Empleado.objects.all()

    if buscar:
        empleados = empleados.filter(
            Q(cedula__icontains=buscar) |
            Q(nombres__icontains=buscar) |
            Q(apellidos__icontains=buscar) |
            Q(correo__icontains=buscar)
        )

    return render(request, 'empleado_list.html', {
        'empleados': empleados
    })

def empleado_crear(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_listar')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado_form.html', {'form': form})

def empleado_editar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado_listar')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado_form.html', {'form': form})
