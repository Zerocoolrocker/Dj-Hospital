from django import forms
from .models import Doctor

class RegistroDoctorForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    class Meta:
        model = Doctor
        exclude = ('usuario',)
        # fields = ["nombre", "apellido", "identificacion", "username", "email", "password"]
