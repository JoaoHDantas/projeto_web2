from rest_framework import viewsets
from appteste import models
from appteste.api import serializers


class PixelsViewSet(viewsets.ModelViewSet):
    queryset = models.Pixels.objects.all()
    serializer_class = serializers.Pixels
