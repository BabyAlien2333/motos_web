from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

class Moto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    cilindrada = models.IntegerField()
    potencia = models.IntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=0)

    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='motos/', null=True, blank=True)

    def promedio_estrellas(self):
        promedio = self.resenas.aggregate(Avg('estrellas'))['estrellas__avg']
        return round(promedio, 1) if promedio else 0

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class Resena(models.Model):
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name='resenas')
    
    

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    comentario = models.TextField()
    estrellas = models.IntegerField()
    imagen = models.ImageField(upload_to='resenas/', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.moto}"

