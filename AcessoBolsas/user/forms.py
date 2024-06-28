from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate
from user.models import User


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Obrigatório! Informe o seu email.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'nome', 'password1', 'password2', 'telefone', 'dataNascimento', 'sexo', 'fotoPerfil')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'nome', 'telefone', 'dataNascimento', 'sexo', 'fotoPerfil')

    def save(self, commit=True):
        user = self.instance
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.nome = self.cleaned_data['nome']
        user.telefone = self.cleaned_data['telefone']
        user.dataNascimento = self.cleaned_data['dataNascimento']
        user.sexo = self.cleaned_data['sexo']

        if self.cleaned_data['fotoPerfil']:
            user.fotoPerfil = self.cleaned_data['fotoPerfil']

        if commit:
            user.save()

        return user

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" já sendo utilizado.' % email)
        
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" já sendo utilizado.' % username)
        

class UserAuthForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
    
    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Usuário ou senha inválidos.')