from django.db import models

# Create your models here.
class ParteCuerpo(models.Model):
    nombre = models.CharField(max_length=48)

class Problema(models.Model):
    nombre = models.CharField(max_length=48)

class Presente(models.Model):
    zona    = models.ForeignKey(ParteCuerpo)
    sintoma = models.ForeignKey(Problema)

class Causa(models.Model):
    nombre          = models.CharField(max_length=48)
    descripcion     = models.CharField(max_length=256)
    sintomas        =  models.CharField(max_length=256)
    recomendaciones = models.CharField(max_length=256)

class OrigenProblema(models.Model):
    problema = models.ForeignKey(Problema)
    causa    = models.ForeignKey(Causa)
