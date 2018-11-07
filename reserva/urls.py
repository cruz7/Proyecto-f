from django.conf.urls import url
from . import views

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    url(r'^$', views.inicio, name ='inicio'),
    url(r'^reserva/lista/$', views.lista_reserva, name ='lista_reserva'),
    url(r'^reserva/nueva/$', views.reserva_nueva, name='reserva_nueva'),
    url(r'^reservareserva/(?P<pk>[0-9]+)/detalle/$', views.detalle_reserva, name='detalle_reserva'),
    url(r'^reservareserva/(?P<pk>[0-9]+)/editar/$', views.editar_reserva, name='editar_reserva'),
    url(r'^reserva/(?P<pk>\d+)/eliminar/$', views.eliminar_reserva, name='eliminar_reserva'),
    url(r'^vuelo/nuevo/$', views.vuelo_nuevo, name='vuelo_nuevo'),
    url(r'^pasajero/nuevo/$', views.pasajero_nuevo, name='pasajero_nuevo'),

    url(r'^vuelo/lista/$', views.lista_vuelo, name ='lista_vuelo'),
    url(r'^pasajero/lista/$', views.lista_pasajero, name ='lista_pasajero'),
    ]
