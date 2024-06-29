from django import forms
from scholarship.models import Scholarship

class ScholarshipRegisterForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['titulo', 'tipoBolsa', 'descricao', 'dataPrazo', 'fotoPerfil']

class ScholarshipUpdateForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['titulo', 'tipoBolsa', 'descricao', 'dataPrazo', 'fotoPerfil']

    def save(self, commit=True):
        scholarship = self.instance
        scholarship.titulo = self.cleaned_data['titulo']
        scholarship.tipoBolsa = self.cleaned_data['tipoBolsa']
        scholarship.descricao = self.cleaned_data['descricao']
        scholarship.dataPrazo = self.cleaned_data['dataPrazo']

        if self.cleaned_data['fotoPerfil']:
            scholarship.fotoPerfil = self.cleaned_data['fotoPerfil']

        if commit:
            scholarship.save()
        return scholarship
