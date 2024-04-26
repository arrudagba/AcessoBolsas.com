from django.db import models
from django.contrib.auth.models import User

class PerfilInstituicao(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    contato = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    descricao = models.TextField()
    foto_perfil = models.ImageField(upload_to='perfil_instituicao', default='default.jpg')

    def __str__(self):
        return self.nome