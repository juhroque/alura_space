from django.db import models
from datetime import datetime

# Create your models here.

class Fotografia(models.Model):

    opcoes_categoria = [ # deve ser uma tupla pois o charfield apenas entende assim
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')

    ]

    nome = models.CharField(max_length=100, null=False, blank=False) # -> cria um campo de caracteres de máximo 100 caracteres, e que não pode ser nulo e vazio
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_categoria, default='')
    descricao = models.TextField(null=False, blank=False) # campo de texto
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicar = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now(), blank=False)


    def __str__(self):
        return f'Fotografia [nome={self.nome}]' # boa prática