from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    email = models.EmailField()
    curso = models.CharField(max_length=50)