from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import PasajeroVueloForm, VueloForm, PasajeroForm
from reserva.models import Vuelo, Pasajero, PasajeroVuelo

# Create your views here.

def reserva_nueva(request):
    if request.method == 'POST':
        formulario = PasajeroVueloForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Reserva Guardada Exitosamente')
    else:
        formulario = PasajeroVueloForm()
    return render(request, 'reserva/reserva_editar.html', {'formulario': formulario})

def vuelo_nuevo(request):
    if request.method == 'POST':
        formulario = VueloForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Vuelo Registrado Exitosamente')
    else:
        formulario = VueloForm()
    return render(request, 'reserva/vuelo_editar.html', {'formulario': formulario})

def pasajero_nuevo(request):
    if request.method == 'POST':
        formulario = PasajeroForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Pasajero Registrado Exitosamente')
    else:
        formulario = PasajeroForm()
    return render(request, 'reserva/pasajero_editar.html', {'formulario': formulario})

def lista_reserva(request):
    reserva = PasajeroVuelo.objects.all()
    return render(request, 'reserva/listar_reserva.html', {'reserva': reserva})

def detalle_reserva(request, pk):
     reserva = get_object_or_404(PasajeroVuelo,pk=pk)
     vuelo = Vuelo.objects.all()
     pasajero = Pasajero.objects.all()
     return render(request,"reserva/detalle_reserva.html",{'reserva':reserva,'vuelo':vuelo,'pasajero':pasajero})

def eliminar_reserva(request, pk):
    reserva = get_object_or_404(PasajeroVuelo, pk=pk)
    reserva.delete()
    return redirect('lista_reserva')

def editar_reserva(request, pk):
    reserva = get_object_or_404(PasajeroVuelo,pk=pk)
    if request.method == 'POST':
        formulario = PasajeroVueloForm(request.POST, request.FILES, instance=reserva)
        if formulario.is_valid():
            reserva = formulario.save()
            reserva.save()
            return redirect('detalle_reserva', pk=reserva.pk)

    else:
        formulario = PasajeroVueloForm(instance=reserva)
    return render(request, 'reserva/reserva_editar.html', {'formulario': formulario})