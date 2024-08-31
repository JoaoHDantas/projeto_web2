from rest_framework import routers
from appteste.api import viewsets

appteste_router = routers.DefaultRouter()
appteste_router.register( 'pixels' , viewsets.PixelsViewSet)