from django.urls import path
from odsApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.home, name="home"),

]