from django.shortcuts import render

def home(request):
	return render(request, "odsApp/index.html")

def objetivo1(request):
	return render(request, "odsApp/objetivo1.html")