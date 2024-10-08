from django.contrib import admin

# Register your models here.
from .models import Biblioteca,Autor,Libro

admin.site.register(Biblioteca)
admin.site.register(Autor)
admin.site.register(Libro)