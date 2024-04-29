from django.db import models

# Create your models here.


class Institution(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False, unique=True)
    contato = models.CharField(max_length=50, null=False, blank=False)
    endereco = models.CharField(max_length=255, null=True, blank=True, )
    descricao = models.CharField(max_length=1000, null=False, blank=False)
    #foto_perfil = models.ImageField(upload_to='perfil_instituicao', default='default.jpg')

    def __str__(self):
        return self.nome