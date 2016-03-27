from django import forms
from .models import Doctor

class RegistroDoctorForm(forms.ModelForm):
	username = forms.TextInput()
	email = forms.EmailField()
	password = forms.PasswordInput()

	class Meta:
		model = Doctor
		fields = ["nombre", "apellido", "identificacion", "username", "email", "password"]