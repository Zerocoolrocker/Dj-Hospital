from django.db import models

class Persona(models.Model):

	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	identificacion = models.CharField(max_length=50)

class Paciente(Persona):

	habitacion = models.CharField(max_length=50)
	fecha_ingreso = models.DateField()
	diagnostico = models.CharField(max_length=1000000)
	