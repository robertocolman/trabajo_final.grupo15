from django.shortcuts import render, redirect
from .forms import CustomUserCreationForms
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
	return render(request, "odsApp/index.html")

def objetivo1(request):
	return render(request, "odsApp/objetivo1.html")

def registro(request):
	data ={
		'form': CustomUserCreationForms()
	}

	if request.method == 'POST':
		formulario = CustomUserCreationForms(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
			login(request, user)
			messages.success(request, "te has registrado correctamente")
			return redirect(to="home")
		data["form"] = formulario
	return render(request, "registration/registro.html", data)
