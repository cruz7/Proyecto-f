from django import forms
from .models import Vuelo, Pasajero, PasajeroVuelo

class PasajeroVueloForm(forms.ModelForm):

    class Meta:
        model = PasajeroVuelo
        fields = [
            'nombre',
            'foto',
            'detalle',
            'vue',
            'pas',
        ]
        labels = {
            'nombre': 'Nombre',
            'foto': 'Foto',
            'detalle': 'Detalle',
            'vue': 'Vue',
            'pas': 'Pas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'detalle': forms.TextInput(attrs={'class': 'form-control'}),
            'vue': forms.Select(attrs={'class': 'form-control'}),
            'pas': forms.CheckboxSelectMultiple(),
        }

class VueloForm(forms.ModelForm):

    class Meta:
        model = Vuelo
        fields = [
            'destinoVuelo',
            'fechaSalida',
            'fechaLlegada',
        ]

class PasajeroForm(forms.ModelForm):

    class Meta:
        model = Pasajero
        fields = [
            'nombresPasajero',
            'apellidosPasajero',
            'direccionPasajero',
            'edadPasajero',
            'telefonoPasajero',
        ]
