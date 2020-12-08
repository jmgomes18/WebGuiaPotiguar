from django.db import models

class Empresa(models.Model):

    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    class Meta:

        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.razao_social
