from django.db import models
from django.utils.text import slugify
from random import randint
from django.db.models.signals import post_delete, pre_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

SLUG_LIST = []

class AdminMyAccount(BaseUserManager):

    def create_user(self, username, email, nome,  password = None):
        if not username:
            raise ValueError("Usuário precisa ter um nome de usuário.")
        if not email:
            raise ValueError("Usuário precisa ter um email.")
        if not nome:
            raise ValueError("Usuário precisa ter um nome.")
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nome = nome,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, nome, password):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            nome = nome,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )

    id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    username = models.CharField(help_text='Informe o nome de usuário', max_length=100, null=False, blank=False, unique=True)

    nome = models.CharField(help_text='Informe o nome', max_length=100, null=False, blank=False)

    email = models.EmailField(help_text='Informe o email', max_length=254, null=False, blank=False, unique=True) 

    telefone = models.CharField(help_text='Informe o numéro de telefone', max_length=20, null=True, blank=True)

    dataNascimento = models.DateField(help_text='Informe a data de nascimento', null=True, blank=True)

    sexo = models.CharField(help_text='Informe o sexo', max_length=1, null=True, blank=True, choices=SEXO_CHOICES)

    fotoPerfil = models.ImageField(upload_to='perfil_usuario', default='default.jpg', null=True, blank=True)

    slug = models.SlugField(blank=True, unique=True)

    is_admin = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=False)
    
    is_superuser = models.BooleanField(default=False)


    objects = AdminMyAccount()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=['nome','email']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    
def pre_save_user_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug_random = 0
        while slug_random not in SLUG_LIST:
            slug_random = randint(1, 1000)
            SLUG_LIST.append(slug_random)

        instance.slug = slugify(instance.username + "-" + str(slug_random))

pre_save.connect(pre_save_user_receiver, sender=User)