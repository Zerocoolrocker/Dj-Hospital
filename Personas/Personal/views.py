from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from .models import Doctor
from .forms import RegistroDoctorForm

from ipdb import set_trace

class RegistroDoctor(CreateView):
	model = Doctor
	form_class = RegistroDoctorForm
	template_name = "registro_personal.html"
	success_url = reverse_lazy("home")
	fields  = ["nombre","apellido", "identificacion"]


	def post(self, request, *args, **kwargs):

		user = User.objects.create_user(
			request.POST["username"],
			request.POST["email"],
			request.POST["pass"],
		)
		#agregar id del usuario al request
		super(RegistroDoctor, self).post(request, args, kwargs)


	# def get_context_data(self, **kwargs):
	# 	context["user_form"] = 
	# 	super(RegistroDoctor, self).get_context_data(**kwargs)