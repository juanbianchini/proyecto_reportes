from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import AsistenciaViewSet 


router = DefaultRouter()
router.register('asistencias', AsistenciaViewSet)

urlpatterns = router.urls