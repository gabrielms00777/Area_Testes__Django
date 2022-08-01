from django.db import models

class Clientes(models.Model):
    status = (
        ('Mesalidade', 'Mesalidade'),
        ('Anuidade', 'Anuidade'),
        ('Sem Contrato', 'Sem Contrato'))
    nome = models.CharField(max_length=100)
    cnpj = models.IntegerField(unique=True,)
    status = models.CharField(max_length=100, choices=status)

    def __str__(self):
        return f'{self.nome} - {self.cnpj}'
