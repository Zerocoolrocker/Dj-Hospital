from django.db import models


class Persona(models.Model):

	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	identificacion = models.CharField(max_length=50)


	