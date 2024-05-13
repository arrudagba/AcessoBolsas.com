from django import forms
from scholarship.models import Scholarship

class ScholarshipRegisterForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['titulo', 'tipoBolsa', 'descricao', 'fotoPerfil']

class ScholarshipUpdateForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['titulo', 'tipoBolsa', 'descricao', 'fotoPerfil']

        def save(self, commit=True):
            scholarship = self.instance
            scholarship.titulo = self.cleaned_data['titulo']
            scholarship.tipoBolsa = self.cleaned_data['tipoBolsa']
            scholarship.descricao = self.cleaned_data['descricao']

            if self.cleaned_data['fotoPerfil']:
                scholarship.fotoPerfil = self.cleaned_data['fotoPerfil']

            if commit:
                scholarship.save()

            return scholarship
