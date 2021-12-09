from django.urls import path
from odsApp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import registro


urlpatterns = [
	path('', views.home, name="home"),
	path('objetivo1', views.objetivo1, name="objetivo1"),
	path('registro', registro, name="registro"),

	
]