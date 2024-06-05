from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import User


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Obrigatório! Informe o seu email.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'nome', 'password1', 'password2', 'telefone', 'dataNascimento', 'sexo')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'nome', 'telefone', 'dataNascimento', 'sexo')

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