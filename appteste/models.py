from django.db import models

# Create your models here.


class Pixels(models.Model):
    nickname = models.CharField(max_length=200)
    nome = models.CharField(max_length=200, blank=True, null=True)
    comentario = models.TextField()
    upload = models.FileField(upload_to='pixels/', null=True, blank=True)

