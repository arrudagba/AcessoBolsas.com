from django import forms
from institution.models import Institution

class InstitutionRegisterForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['nome', 'cnpj', 'email', 'contato', 'endereco', 'descricao', 'fotoPerfil']

class InstitutionUpdateForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['nome', 'cnpj', 'email', 'contato', 'endereco', 'descricao', 'fotoPerfil']

    def save(self, commit=True):
        institution = self.instance
        institution.nome = self.cleaned_data['nome']
        institution.cnpj = self.cleaned_data['cnpj']
        institution.email = self.cleaned_data['email']
        institution.contato = self.cleaned_data['contato']
        institution.endereco = self.cleaned_data['endereco']
        institution.descricao = self.cleaned_data['descricao']

        if self.cleaned_data['fotoPerfil']:
            institution.fotoPerfil = self.cleaned_data['fotoPerfil']

        if commit:
            institution.save()
        return institution

    def clean_email(self):
        email = self.cleaned_data['email']
        if Institution.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('Email "%s" já está sendo utilizado.' % email)
        return email

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if Institution.objects.exclude(pk=self.instance.pk).filter(nome=nome).exists():
            raise forms.ValidationError('Nome "%s" já está sendo utilizado.' % nome)
        return nome

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        if Institution.objects.exclude(pk=self.instance.pk).filter(cnpj=cnpj).exists():
            raise forms.ValidationError('CNPJ "%s" já está sendo utilizado.' % cnpj)
        return cnpj