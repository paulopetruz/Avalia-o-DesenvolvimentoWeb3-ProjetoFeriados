from django.db import models

# Create your models here.
class FeriadoModel(models.Model):
    nome = models.CharField('feriado', max_length=255)
    data = models.DateField('data')

    def __str__(self):
        return self.nome