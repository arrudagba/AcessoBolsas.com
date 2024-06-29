from django.db import models
from random import randint
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save

# Create your models here.

SLUG_LIST = []

class Scholarship(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    titulo = models.CharField(help_text='Título da bolsa', max_length=150, null=False, blank=False)

    tipoBolsa = models.CharField(help_text='Tipo da bolsa', max_length=100, null=False, blank=False)

    descricao = models.TextField(help_text='Descrição da bolsa', max_length=5000, null=False, blank=False)

    dataPostada = models.DateField(help_text='Data da postagem da bolsa', auto_now_add=True, verbose_name='Data da postagem')

    dataAtualizada = models.DateField(help_text='Data da atualização da bolsa', auto_now=True, verbose_name='Data da atualização')

    instituicao = models.ForeignKey('institution.Institution', on_delete=models.CASCADE)

    fotoPerfil = models.ImageField(upload_to='scholarship', default='default.jpg', null=True, blank=True)

    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.titulo
    
def pre_save_scholarship_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug_random = 0
        while slug_random not in SLUG_LIST:
            slug_random = randint(1, 1000)
            SLUG_LIST.append(slug_random)

        instance.slug = slugify(instance.instituicao.nome + "-" + str(slug_random))

pre_save.connect(pre_save_scholarship_receiver, sender=Scholarship)