from django.db import models
from personas.models import Persona

# Modelo Asistencia
class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="asistencias")
    fecha_hora = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=200)
    tipo_asistencia = models.CharField(max_length=200)
    geolocalizacion = models.CharField(max_length=255, blank=True, null=True)
    detalle = models.TextField()
    asistencia_prolongada = models.BooleanField(default=False)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Asistencia a {self.persona.nombre} {self.persona.apellido} - {self.tipo_asistencia} ({self.fecha_hora})"



