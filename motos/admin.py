from django.contrib import admin
from .models import Moto, Resena

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'precio')

