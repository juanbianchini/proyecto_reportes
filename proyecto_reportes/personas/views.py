from .serializers import PersonaSerializer
from .models import Persona
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET"])
def list_persona(request):
    personas = Persona.objects.all()
    serializer = PersonaSerializer(personas, many=True)
    return Response(serializer.data)
    

