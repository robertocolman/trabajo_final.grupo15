from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Categoria(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField('nombre de la Categoria', max_length=100, null = False, blank = False)
	estado = models.BooleanField('Categoria Activada/Categoria no activada', default = True)
	Fecha_creacion = models.DateField('fecha de Creación', auto_now = False, auto_now_add = True)

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def __str__(self):
		return self.nombre

class Autor(models.Model):
	id = models.AutoField(primary_key = True)
	nombres = models.CharField('Nombres autor', max_length= 90, blank= False, null= False)
	apellidos = models.CharField('Apellidos autor', max_length= 90, blank= False, null= False)
	estado = models.BooleanField('Autor Activo/No activo', default = True)
	fecha_creacion = models.DateField('fecha de creación', auto_now = False, auto_now_add = True)


	class Meta:
		verbose_name = 'Autor'
		verbose_name_plural = 'Autores'

	def __str__(self):
			return "{0},{1}".format(self.nombres, self.apellidos)


class Post(models.Model):
	id = models.AutoField(primary_key = True)
	titulo = models.CharField('titulo', max_length= 90, blank= False, null= False)
	#slug = models.CharField('slug', max_length= 100, blank= False, null= False)
	descripcion = models.CharField('descripcion', max_length= 100, blank= False, null= False)
	contenido = models.TextField()
	imagen = models.URLField( max_length= 255, blank= True, null= True)
	autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	estado = models.BooleanField('publicado/no Publicado', default = True)
	fecha_creacion = models.DateField('fecha de creación', auto_now = False, auto_now_add = True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def __str__(self):
		return self.titulo
