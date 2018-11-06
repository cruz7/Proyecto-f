from django.db import models
from django.contrib import admin

# Create your models here.

class Vuelo(models.Model):

    destinoVuelo  =   models.CharField(max_length=60, verbose_name="Destino")
    fechaSalida  =   models.DateField(max_length=60, verbose_name="FechaS")
    fechaLlegada  =   models.DateField(max_length=60, verbose_name="FechasL")

    class Meta:
                verbose_name="Vuelo"
                verbose_name_plural="Vuelos"
                ordering = ["-destinoVuelo"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.destinoVuelo

class Pasajero(models.Model):

    nombresPasajero  =   models.CharField(max_length=60)
    apellidosPasajero  =   models.CharField(max_length=60)
    direccionPasajero  =   models.CharField(max_length=60)
    edadPasajero  =   models.CharField(max_length=60)
    telefonoPasajero  =   models.IntegerField()

    class Meta:
                verbose_name="Pasajero"
                verbose_name_plural="Pasajeros"
                ordering = ["-apellidosPasajero"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombresPasajero


class PasajeroVuelo(models.Model):

    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="fotodestino",null=True,blank=True)
    detalle = models.CharField(max_length=200)
    vue = models.ForeignKey(Vuelo,on_delete=models.CASCADE,related_name="keyvue", help_text="Ingrese un numeros entero")
    pas = models.ManyToManyField(Pasajero,verbose_name="Pasajero",related_name="keypas")

    class Meta:
                verbose_name="PasajeroVuelo"
                verbose_name_plural="PasajerosVuelos"
                ordering = ["-vue"]

    def __str__(self):
        return self.nombre
