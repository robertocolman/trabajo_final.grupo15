from django.urls import path
from odsApp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import registro


urlpatterns = [
	path('', views.home, name="home"),
	path('objetivo1', views.objetivo1, name="objetivo1"),
	path('objetivo2', views.objetivo2, name="objetivo2"),
	path('objetivo3', views.objetivo3, name="objetivo3"),
	path('objetivo4', views.objetivo4, name="objetivo4"),
	path('objetivo5', views.objetivo5, name="objetivo5"),
	path('objetivo6', views.objetivo6, name="objetivo6"),
	path('objetivo7', views.objetivo7, name="objetivo7"),
	path('objetivo8', views.objetivo8, name="objetivo8"),
	path('objetivo9', views.objetivo9, name="objetivo9"),
	path('objetivo10', views.objetivo10, name="objetivo10"),
	path('objetivo11', views.objetivo11, name="objetivo11"),
	path('objetivo12', views.objetivo12, name="objetivo12"),
	path('objetivo13', views.objetivo13, name="objetivo13"),
	path('objetivo14', views.objetivo14, name="objetivo14"),
	path('objetivo15', views.objetivo15, name="objetivo15"),
	path('objetivo16', views.objetivo16, name="objetivo16"),
	path('objetivo17', views.objetivo17, name="objetivo17"),
	path('leermas', views.leermas, name="leermas"),
	path('registro', registro, name="registro"),
	path("Admin/Listar/", views.ListarAdmin.as_view(), name="Admin_Listar"),
	path("Admin/Nuevo/", views.NuevoAdmin.as_view(), name="Admin_Nuevo"),

	
]