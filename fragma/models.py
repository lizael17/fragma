from django.db import models


class cadastro(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    chave = models.CharField(max_length=100)
    doar = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nome
    

