from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False, unique=True)
    contato = models.CharField(max_length=50, null=False, blank=False)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=False, blank=False)
    foto_perfil = models.ImageField(upload_to='perfil_instituicao', default='default.jpg')
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
