from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from .models import Doctor
import pickle
from .forms import RegistroDoctorForm

from ipdb import set_trace

class RegistroDoctor(CreateView):
	model = Doctor
	form_class = RegistroDoctorForm
	template_name = "registro_personal.html"
	success_url = reverse_lazy("home")
	# fields  = ["nombre","apellido", "identificacion"]


	def form_valid(self, form):
            cd = form.cleaned_data
            user = User.objects.create_user(cd.get("username"),cd.get("email"),cd.get("password"))
            form.instance.usuario = user
            return super(RegistroDoctor, self).form_valid(form)
