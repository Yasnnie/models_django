from django.db import models

# Create your models here.
class Disco(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    selo_fonografico = models.CharField(max_length=50)
    ano = models.IntegerField()
    pais = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome