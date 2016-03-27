from django.db import models


class Persona(models.Model):

	persona_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	identificacion = models.CharField(max_length=50)


	