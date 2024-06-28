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
            if self.is_valid():
                email = self.cleaned_data['email']
                try:
                    institution = Institution.objects.exclude(pk=self.instance.pk).get(email=email)
                except Institution.DoesNotExist:
                    return email
                raise forms.ValidationError('Email "%s" já sendo utilizado.' % email)
        
        def clean_nome(self):
            if self.is_valid():
                nome = self.cleaned_data['nome']
                try:
                    institution = Institution.objects.exclude(pk=self.instance.pk).get(nome=nome)
                except Institution.DoesNotExist:
                    return nome
                raise forms.ValidationError('Nome "%s" já sendo utilizado.' % nome)
        
        def clean_cnpj(self):
            if self.is_valid():
                cnpj = self.cleaned_data['cnpj']
                try:
                    institution = Institution.objects.exclude(pk=self.instance.pk).get(cnpj=cnpj)
                except Institution.DoesNotExist:
                    return cnpj
                raise forms.ValidationError('CNPJ "%s" já sendo utilizado.' % cnpj)