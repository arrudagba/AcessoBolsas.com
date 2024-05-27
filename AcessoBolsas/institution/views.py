from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from institution.models import Institution
from institution.forms import InstitutionRegisterForm, InstitutionUpdateForm

# Create your views here.

def createInstitution(request):
    context = {}

    form = InstitutionRegisterForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        institution = form.save(commit=False)
        institution.save()
        form = InstitutionRegisterForm()
        messages.success(request, 'Instituição cadastrada com sucesso!')
        return redirect('home')
    
    context['form'] = form
    return render(request, 'institution/createInstitution.html', context)


def editInstitution(request, slug):
    context = {}

    institution = get_object_or_404(Institution, slug=slug)

    if request.POST == 'POST':
        form = InstitutionUpdateForm(request.POST, request.FILES or None,
                                     instance=institution)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Instituição atualizada com sucesso!')
            institution = obj
            return redirect('home')
        
    form = InstitutionUpdateForm(
        initial={
            'nome': institution.nome,
            'cnpj': institution.cnpj,
            'contato': institution.contato,
            'endereco': institution.endereco,
            'descricao': institution.descricao,
            'fotoPerfil': institution.fotoPerfil,
        }
    )

    context['form'] = form
    return render(request, 'institution/editInstitution.html', context)


def viewInstitution(request, slug):
    context = {}
    institution = get_object_or_404(Institution, slug=slug)
    context['institution'] = institution
    return render(request, 'institution/viewInstitution.html', context)


def deleteInstitution(request, slug):
    context = {}
    institution = get_object_or_404(Institution, slug=slug)
    if request.POST:
        institution.fotoPerfil.delete()
        institution.delete()
        messages.success(request, 'Instituição excluída com sucesso!')
        return redirect('home')
    
    context['institution'] = institution
    return render(request, 'institution/deleteInstitution.html', context)


def listInstitutions(request):
    context = {}
    institutions = Institution.objects.all()
    context['institutions'] = institutions
    return render(request,'institution/listInstitutions.html', context)
