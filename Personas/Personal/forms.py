from django import forms
from .models import Doctor

class RegistroDoctorForm(forms.ModelForm):

    def __init__(self, user_id, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)

        # set the user_id as an attribute of the form
        self.usuario_id = usuario_id


	username = forms.CharField(max_length=50)
	email = forms.EmailField()
	password = forms.CharField(max_length=100)

	class Meta:
		model = Doctor
		exclude = ('usuario',)
		# fields = ["nombre", "apellido", "identificacion", "username", "email", "password"]