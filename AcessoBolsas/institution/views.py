from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
import string
from django.views.decorators.csrf import csrf_protect
from institution.models import Institution
from institution.forms import InstitutionRegisterForm, InstitutionUpdateForm

# Create your views here.

@csrf_protect
def createInstitution(request):
    context = {}

    form = InstitutionRegisterForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        institution = form.save(commit=False)
        institution.save()
        form = InstitutionRegisterForm()
        messages.success(request, 'Instituição cadastrada com sucesso!')
        request.session['logged'] = False
        request.session['institution_id'] = None
        return redirect('home')
    
    context['form'] = form
    return render(request, 'institution/createInstitution.html', context)


def editInstitution(request, slug):
    context = {}

    institution = get_object_or_404(Institution, slug=slug)

    if (institution.logged == False):
        return redirect('home')

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
            'email': institution.email,
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

    if (institution.logged == False):
        return redirect('home')
    
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

def generate_random_password(length=8):

    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def loginInstitution(request):
    context = {}
    logout(request)
    
    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        try:
            institution = Institution.objects.get(cnpj=cnpj)

            # Generate a random password
            password = generate_random_password()
            institution.password = password
            institution.save()

            # Send email to institution with the generated password
            send_mail(
                'Sua senha de login',
                f'Sua senha é: {password}',
                settings.DEFAULT_FROM_EMAIL,
                [institution.email],
                fail_silently=False,
            )
            context['message'] = 'A senha foi enviada para o email cadastrado. Verifique a sua caixa de entrada no email.'
            context['cnpj'] = cnpj
            return render(request, 'institution/verify_password.html', context)
        except Institution.DoesNotExist:
            context['error'] = 'Instituição com esse CNPJ não existe.'
    
    return render(request, 'institution/loginInstitution.html', context)

def logoutInstitution(request):
    institution = Institution.objects.get(id=request.session['institution_id'])
    institution.logged = False
    request.session['logged'] = False
    request.session['institution_id'] = None
    institution.save()
    return redirect('home')

def verify_password(request):
    context = {}

    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        password = request.POST['password']
        institution = Institution.objects.get(cnpj=cnpj)
        if password == institution.password:
            # Password is correct, log the institution in
            institution.logged = True
            institution.save()
            request.session['logged'] = True
            request.session['institution_id'] = institution.id
            return redirect('home')
        else:
            context['error'] = 'Senha incorreta. Tente novamente.'
    
    return render(request, 'institution/verify_password.html', context)