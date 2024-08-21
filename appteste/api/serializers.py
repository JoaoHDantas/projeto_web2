from rest_framework import serializers
from appteste import models

class Pixels(serializers.ModelSerializer):
    class Meta:
        model = models.Pixels
        fields = '__all__'