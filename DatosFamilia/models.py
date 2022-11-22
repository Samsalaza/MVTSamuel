from django.db import models
from .models import models

# Create your models here.

class Familiares (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    fecha_nacimiento=models.DateField()

    def __str__(self):
        return self.nombre+" "+self.apellido
    
    
    