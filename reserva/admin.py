from django.contrib import admin
from reserva.models import Vuelo, Pasajero, PasajeroVuelo

# Register your models here.
#Registramos nuestras clases principales.
admin.site.register(Vuelo)
admin.site.register(Pasajero)
admin.site.register(PasajeroVuelo)
