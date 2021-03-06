from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import Home
from Personas.Pacientes.views import RegistroPaciente, EditarPaciente, Pacientes, DetallesPaciente
from Personas.Personal.views import RegistroDoctor

urlpatterns = [
    # Examples:
    # url(r'^$', 'hospital.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', Home.as_view(), name="home"),
    # url(r'^pacientes/registro/', "Personas.views.registro_paciente"),
    url(r'^pacientes/$', Pacientes.as_view(), name="lista-pacientes"),
    url(r'^pacientes/registro/$', RegistroPaciente.as_view(), name="registro-paciente"),
    url(r'^pacientes/editar/(?P<pk>[\d]+)/$', EditarPaciente.as_view(), name="registro-paciente"),
    url(r'^pacientes/(?P<pk>[\d]+)/$', DetallesPaciente.as_view(), name="detalles-paciente"),
    url(r'^personal/doctores/registro/$', RegistroDoctor.as_view(), name="registro-doctor"),
]
