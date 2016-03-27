from django.db import models
from Personas.models import Persona


class Paciente(Persona):

	habitacion = models.CharField(max_length=50)
	fecha_ingreso = models.DateField()
	diagnostico = models.CharField(max_length=1000000)
