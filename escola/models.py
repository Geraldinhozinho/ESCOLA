from django.db import models

# Create your models here.

class Professor(models.Model):
    nome= models.CharField(max_length=150)
    email= models.EmailField()
    celular= models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome= models.CharField(max_length=150)
    carga_horaria= models.IntegerField()
    codigo= models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    