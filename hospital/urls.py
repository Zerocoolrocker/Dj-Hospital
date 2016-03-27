from django.conf.urls import patterns, include, url
from django.contrib import admin
from Personas.views import RegistroPaciente, Home, Pacientes

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hospital.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', Home.as_view(), name="home"),
    # url(r'^pacientes/registro/', "Personas.views.registro_paciente"),
    url(r'^pacientes/$', Pacientes.as_view(), name="lista-pacientes"),
    url(r'^pacientes/registro/$', RegistroPaciente.as_view(), name="registro-paciente"),
)