from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from Personas.models import Paciente



class Home(TemplateView):
	template_name = "home.html"


class RegistroPaciente(CreateView):
	model = Paciente
	template_name = "registro.html"
	success_url = reverse_lazy("home")
	fields = ["nombre", "identificacion", "apellido", "identificacion", "habitacion", "fecha_ingreso", "diagnostico"]


class EditarPaciente(UpdateView):
	model = Paciente
	template_name = "registro.html"
	success_url = reverse_lazy("home")
	fields = ["nombre", "identificacion", "apellido", "identificacion", "habitacion", "fecha_ingreso", "diagnostico"]

class Pacientes(ListView):

	model = Paciente
	template_name = "paciente_list.html"
