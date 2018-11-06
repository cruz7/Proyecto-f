# Generated by Django 2.1.3 on 2018-11-05 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombresPasajero', models.CharField(max_length=60)),
                ('apellidosPasajero', models.CharField(max_length=60)),
                ('direccionPasajero', models.CharField(max_length=60)),
                ('edadPasajero', models.CharField(max_length=60)),
                ('telefonoPasajero', models.IntegerField(max_length=60)),
            ],
            options={
                'verbose_name': 'Pasajero',
                'verbose_name_plural': 'Pasajeros',
                'ordering': ['-apellidosPasajero'],
            },
        ),
        migrations.CreateModel(
            name='PasajeroVuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotodestino')),
                ('detalle', models.CharField(max_length=200)),
                ('pas', models.ManyToManyField(related_name='keypas', to='reserva.Pasajero', verbose_name='Pasajero')),
            ],
            options={
                'verbose_name': 'PasajeroVuelo',
                'verbose_name_plural': 'PasajerosVuelos',
                'ordering': ['-vue'],
            },
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinoVuelo', models.CharField(max_length=60, verbose_name='Destino')),
                ('fechaSalida', models.DateField(max_length=60, verbose_name='FechaS')),
                ('fechaLlegada', models.DateField(max_length=60, verbose_name='FechasL')),
            ],
            options={
                'verbose_name': 'Vuelo',
                'verbose_name_plural': 'Vuelos',
                'ordering': ['-destinoVuelo'],
            },
        ),
        migrations.AddField(
            model_name='pasajerovuelo',
            name='vue',
            field=models.ForeignKey(help_text='Ingrese un numeros entero', on_delete=django.db.models.deletion.CASCADE, related_name='keyvue', to='reserva.Vuelo'),
        ),
    ]