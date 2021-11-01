from django.db import models

# Create your models here.

class Tag(models.Model):
    nome = models.CharField(max_length=60, unique=True)
    def __str__(self):
        return self.nome

class Card(models.Model):
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.texto