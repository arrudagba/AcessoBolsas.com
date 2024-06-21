from django.db import models
from random import randint
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save

SLUG_LIST = []

class Institution(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=18, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True, default='default@mail.com')
    contato = models.CharField(max_length=50, null=False, blank=False)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=False, blank=False)
    fotoPerfil = models.ImageField(upload_to='institution', default='default.jpg')
    slug = models.SlugField(blank=True, unique=True)
    checked = models.BooleanField(default=False)
    logged = models.BooleanField(default=False)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome
    

def pre_save_institution_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug_random = 0
        while slug_random not in SLUG_LIST:
            slug_random = randint(1, 1000)
            SLUG_LIST.append(slug_random)
        
        instance.slug = slugify(instance.nome + "-" + str(slug_random))

pre_save.connect(pre_save_institution_receiver, sender=Institution)