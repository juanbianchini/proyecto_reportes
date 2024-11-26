from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Persona
from .serializers import PersonaSerializer
from asistencias.models import Asistencia  
from asistencias.serializers import AsistenciaSerializer  


# En PersonaViewSet
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    @action(detail=True, methods=['get'])
    def historial_asistencias(self, request, pk=None):
        persona = self.get_object()
        asistencias = persona.asistencias.all()
        serializer = AsistenciaSerializer(asistencias, many=True)
        return Response(serializer.data)


