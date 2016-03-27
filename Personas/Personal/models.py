from django.db import models
from django.contrib.auth.models import User
from Personas.models import Persona


class Empleado(models.Model):
	empleado_id = models.AutoField(primary_key=True)

class Doctor(Persona, Empleado):
	usuario = models.OneToOneField(User)
