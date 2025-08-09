from datetime import date
from django.db import models    

class Funcionario(models.Model):    
    nome = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    sobrenome = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    ) 
    data_nascimento = models.DateField(
        null=False,
        blank=False,
        default=date(1990, 1, 1)
    )
    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    remuneracao = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )
    
    objects = models.Manager()
