from django.db import models

class Funcionario(models.Model):

    TIPO = (
        (0, 'Professor(a)'),
        (1, 'Caest'),
    )
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    function = models.IntegerField(choices=TIPO)
