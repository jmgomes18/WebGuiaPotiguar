from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Empresa(models.Model):
        
    CATEGORIA_CHOICES = (
        ('AL','ALIMENTAÇÃO E BEBIDAS'),
        ('AU', 'AUTOMOTIVA'),
        ('SA', 'SAUDE'),
        ('TI', 'TECNOLOGIA DA INFORMAÇÃO'),
        ('SP', 'SERVIÇOS PESSOAIS'),
        ('SE', 'SERVIÇOS ESPECIALIZADOS'),
        ('ED', 'EDUCAÇÃO'),
        ('CO', 'CONSTRUÇÃO'),
        ('VE', 'VESTUÁRIO'),
        ('ET', 'ENTRETENIMENTO')
    )

    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=256, blank=True)
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES, blank=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):      
        return self.razao_social

    def get_absolute_url(self):
        return reverse('empresa_update', kwargs={'pk': self.pk})


    