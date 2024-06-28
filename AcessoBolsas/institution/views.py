from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
import logging
import string
from django.views.decorators.csrf import csrf_protect
from institution.models import Institution
from institution.forms import InstitutionRegisterForm, InstitutionUpdateForm
from scholarship.models import Scholarship
from operator import attrgetter

# Create your views here.

@csrf_protect
def createInstitution(request):
    context = {}
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

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
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

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
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')
    institution = get_object_or_404(Institution, slug=slug)
    context['institution'] = institution
    return render(request, 'institution/viewInstitution.html', context)


def deleteInstitution(request, slug):
    context = {}
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')
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
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')
    institutions = Institution.objects.all()
    context['institutions'] = institutions
    return render(request,'institution/listInstitutions.html', context)

def generate_random_password(length=8):

    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

logger = logging.getLogger(__name__)

def loginInstitution(request):
    context = {}
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        password = request.POST.get('password', None)

        if password:
            # Etapa de verificação de senha
            try:
                institution = Institution.objects.get(cnpj=cnpj)
                if password == institution.password:
                    logout(request)
                    institution.logged = True
                    institution.save()
                    response = redirect('home')
                    response.set_cookie('logged', True)
                    response.set_cookie('slugInstitution', institution.slug)
                    response.set_cookie('nameInstitution', institution.nome)
                    return response
                else:
                    context['error'] = 'Senha incorreta. Tente novamente.'
                    context['cnpj'] = cnpj
            except Institution.DoesNotExist:
                context['error'] = 'Instituição com esse CNPJ não existe.'
        else:
            # Etapa de envio de senha
            try:
                institution = Institution.objects.get(cnpj=cnpj)

                # Gerar uma senha aleatória
                password = generate_random_password()
                institution.password = password
                institution.save()

                # Enviar email para a instituição com a senha gerada
                send_mail(
                    'Sua senha de login',
                    f'Sua senha é: {password}',
                    settings.DEFAULT_FROM_EMAIL,
                    [institution.email],
                    fail_silently=False,
                )
                context['message'] = 'A senha foi enviada para o email cadastrado. Verifique a sua caixa de entrada no email.'
                context['cnpj'] = cnpj
            except Institution.DoesNotExist:
                context['error'] = 'Instituição com esse CNPJ não existe.'
            except Exception as e:
                logger.error(f'Erro ao enviar e-mail: {e}')
                context['error'] = f'Erro ao enviar e-mail: {e}'

    return render(request, 'institution/loginInstitution.html', context)

def logoutInstitution(request):
    institution = Institution.objects.get(slug=request.COOKIES.get('slugInstitution'))
    institution.logged = False
    institution.save()
    response = redirect('home')
    response.set_cookie('logged', False)
    response.set_cookie('slugInstitution', None)
    response.set_cookie('nameInstitution', None)
    return response

def myAccountInstitution(request, slugInstitution):
    context = {}
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')
    
    institution = get_object_or_404(Institution, slug=slugInstitution)
    context['institution'] = institution
    return render(request,'institution/viewInstitution.html', context)

def institutionScholarships(request, slug):
    context = {}
    institution = get_object_or_404(Institution, slug=slug)
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

    query = request.GET.get('q')
    if query:
        scholarships = Scholarship.objects.filter(titulo__icontains=query, instituicao=institution)
    else:
        scholarships = Scholarship.objects.filter(instituicao=institution).order_by('-titulo')
        
    context['scholarships'] = scholarships
    
    return render(request, 'institution/InstitutionScholarships.html', context)
        
    
    