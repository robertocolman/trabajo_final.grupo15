from django.shortcuts import render, redirect
from .forms import CustomUserCreationForms, PostForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


def home(request):
	return render(request, "odsApp/index.html")

def objetivo1(request):
	post = Post.objects.filter(estado = True)
	return render(request, "odsApp/objetivos/objetivo1.html", {'posts': post})

def objetivo2(request):
	return render(request, "odsApp/objetivos/objetivo2.html")

def objetivo3(request):
	return render(request, "odsApp/objetivos/objetivo3.html")

def objetivo4(request):
	return render(request, "odsApp/objetivos/objetivo4.html")

def objetivo5(request):
	return render(request, "odsApp/objetivos/objetivo5.html")

def objetivo6(request):
	return render(request, "odsApp/objetivos/objetivo6.html")

def objetivo7(request):
	return render(request, "odsApp/objetivos/objetivo7.html")

def objetivo8(request):
	return render(request, "odsApp/objetivos/objetivo8.html")

def objetivo9(request):
	return render(request, "odsApp/objetivos/objetivo9.html")

def objetivo10(request):
	return render(request, "odsApp/objetivos/objetivo10.html")

def objetivo11(request):
	return render(request, "odsApp/objetivos/objetivo11.html")

def objetivo12(request):
	return render(request, "odsApp/objetivos/objetivo12.html")

def objetivo13(request):
	return render(request, "odsApp/objetivos/objetivo13.html")

def objetivo14(request):
	return render(request, "odsApp/objetivos/objetivo14.html")

def objetivo15(request):
	return render(request, "odsApp/objetivos/objetivo15.html")

def objetivo16(request):
	return render(request, "odsApp/objetivos/objetivo16.html")

def objetivo17(request):
	return render(request, "odsApp/objetivos/objetivo17.html")

def leermas(request):
	return render(request, "odsApp/objetivos/leermas.html")

def registro(request):
	data ={
		'form': CustomUserCreationForms()
	}

	if request.method == 'POST':
		formulario = CustomUserCreationForms(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
			my_group = Group.objects.get(name='UsuarioLogeado') 
			my_group.user_set.add(user)
			login(request, user)
			messages.success(request, "te has registrado correctamente")
			return redirect(to="home")
		data["form"] = formulario
	return render(request, "registration/registro.html", data)

class ListarAdmin(ListView):
	template_name = "odsApp/admin/listar.html"
	model = Post

class NuevoAdmin(CreateView):
	template_name = "odsApp/admin/nuevo.html"
	model = Post
	form_class = PostForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("home")



'''
class NuevoPost(CreateView):
	template_name = "odsApp/admin/Post"
	model = Post
'''