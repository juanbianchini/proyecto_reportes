from django.db import models

# Modelo Persona
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    apodo = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    telefono_referencia = models.CharField(max_length=15, blank=True, null=True)
    ubicacion = models.TextField()
    lugar_fijo_transitorio = models.BooleanField(default=False)
    datos_contacto = models.TextField(blank=True, null=True)
    centro_vida = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.dni})"
