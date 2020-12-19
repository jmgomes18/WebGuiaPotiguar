from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('registro_empresa', kwargs={'pk': self.pk})

    def __str__(self):      
        return self.razao_social
    