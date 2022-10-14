from django.db import models

# Create your models here.
class Produtos(models.Model):
    descricao = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    codigo = models.IntegerField()
    quantidade = models.IntegerField()

