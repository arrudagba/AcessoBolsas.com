from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class AdminMyAccount(BaseUserManager):

    def create_user(self, username, email, name, password = None):
        if not username:
            raise ValueError("Usuário precisa ter um nome de usuário.")
        if not email:
            raise ValueError("Usuário precisa ter um email.")
        if not name:
            raise ValueError("Usuário precisa ter um nome.")
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            name = name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, name, password):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            name = name,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )

    id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)

    username = models.CharField(help_text='Informe o nome de usuário', max_length=100, null=False, blank=False, unique=True)

    name = models.CharField(help_text='Informe o nome', max_length=100, null=False, blank=False)

    email = models.EmailField(help_text='Informe o email', max_length=254, null=False, blank=False, unique=True) 

    telefone = models.CharField(help_text='Informe o numéro de telefone', max_length=20, null=True, blank=True)

    dataNascimento = models.DateField(help_text='Informe a data de nascimento', null=True, blank=True)

    sexo = models.CharField(help_text='Informe o sexo', max_length=1, null=True, blank=True, choices=SEXO_CHOICES)

    fotoPerfil = models.ImageField(upload_to='perfil_usuario', default='default.jpg', null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=False)
    
    is_superuser = models.BooleanField(default=False)


    objects = AdminMyAccount()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=['username','name','email']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True