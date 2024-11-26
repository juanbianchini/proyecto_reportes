from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import PersonaViewSet 


router = DefaultRouter()
router.register('personas', PersonaViewSet)

urlpatterns = router.urls