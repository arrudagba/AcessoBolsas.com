from django.db import models

# Create your models here.

class Scholarship(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    titulo = models.CharField(help_text='Título da bolsa', max_length=150, null=False, blank=False)

    tipoBolsa = models.CharField(help_text='Tipo da bolsa', max_length=100, null=False, blank=False)

    descricao = models.TextField(help_text='Descrição da bolsa', max_length=5000, null=False, blank=False)

    dataPostada = models.DateField(help_text='Data da postagem da bolsa', auto_now_add=True, verbose_name='Data da postagem')

    dataAtualizada = models.DateField(help_text='Data da atualização da bolsa', auto_now=True, verbose_name='Data da atualização')

    instituicao = models.ForeignKey('institution.Institution', on_delete=models.CASCADE)

    fotoPerfil = models.ImageField(upload_to='perfil_usuario', default='default.jpg', null=True, blank=True)

    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.titulo
