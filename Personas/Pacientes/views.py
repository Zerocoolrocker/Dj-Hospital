from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Paciente


class Pacientes(ListView):
	model = Paciente
	template_name = "paciente_list.html"

class RegistroPaciente(CreateView):
	model = Paciente
	template_name = "registro.html"
	success_url = reverse_lazy("home")


class DetallesPaciente(DetailView):
	model = Paciente
	template_name = "detalles_paciente.html"


class EditarPaciente(UpdateView):
	model = Paciente
	template_name = "registro.html"
	success_url = reverse_lazy("home")