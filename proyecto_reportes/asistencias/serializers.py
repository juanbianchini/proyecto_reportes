from rest_framework import serializers
from .models import Asistencia

#SerializadorAsistencia
class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'