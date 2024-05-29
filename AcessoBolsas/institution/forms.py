from django import forms
from institution.models import Institution

class InstitutionRegisterForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['nome', 'cnpj', 'contato', 'endereco', 'descricao', 'fotoPerfil']

class InstitutionUpdateForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['nome', 'cnpj', 'contato', 'endereco', 'descricao', 'fotoPerfil']

        def save(self, commit=True):
            institution = self.instance
            institution.nome = self.cleaned_data['nome']
            institution.cnpj = self.cleaned_data['cnpj']
            institution.contato = self.cleaned_data['contato']
            institution.endereco = self.cleaned_data['endereco']
            institution.descricao = self.cleaned_data['descricao']

            if self.cleaned_data['fotoPerfil']:
                institution.fotoPerfil = self.cleaned_data['fotoPerfil']

            if commit:
                institution.save()

            return institution