from django.shortcuts import render, redirect, get_object_or_404
from scholarship.forms import ScholarshipRegisterForm, ScholarshipUpdateForm
from django.contrib import messages
from institution.models import Institution
from scholarship.models import Scholarship
from django.http import JsonResponse
from django.http import HttpResponse
import json

# Create your views here.

def createScholarship(request):
    context = {}

    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

    institution = get_object_or_404(Institution, slug=request.COOKIES.get('slugInstitution'))
    if not institution.checked and not institution.logged:
       return redirect("loginInstitution")
    
    form = ScholarshipRegisterForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        scholarship = form.save(commit=False)
        institution_author = institution
        scholarship.instituicao = institution_author
        scholarship.save()
        form = ScholarshipRegisterForm()
        messages.success(request, 'Bolsa cadastrada com sucesso!')
        return redirect('home')
    
    context['form'] = form        
    return render(request, 'scholarship/createScholarship.html', context)


def editScholarship(request, slug):
    context = {}

    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

    scholarship = get_object_or_404(Scholarship, slug=slug)
    institution = scholarship.instituicao

    if not institution.checked or not institution.logged:
        return redirect("loginInstitution")
    
    if request.method == 'POST':
        form = ScholarshipUpdateForm(request.POST, request.FILES, instance=scholarship)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bolsa atualizada com sucesso!')
            return redirect('home')
        else:
            messages.warning(request, 'Erro ao atualizar a bolsa. Tente novamente.')
    else:
        form = ScholarshipUpdateForm(instance=scholarship)

    context['form'] = form
    return render(request, 'scholarship/editScholarship.html', context)


def viewScholarship(request, slug):
    context = {}

    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')
    
    scholarship = get_object_or_404(Scholarship, slug=slug)
    context['scholarship'] = scholarship

    if request.method == 'POST':
        data = json.loads(request.body)
        if 'url' in data:
            url = data.get('url', '')
            print(f"URL recebida: {url}")
            return JsonResponse({'status': 'success', 'url': url})
        elif 'action' in data and data['action'] == 'contact':
            contato = scholarship.instituicao.contato
            print(f"Contato da instituição: {contato}")
            return JsonResponse({'status': 'success', 'contato': contato})

    return render(request, 'scholarship/viewScholarship.html', context)


def deleteScholarship(request, slug):
    context = {}

    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')
    
    scholarship = get_object_or_404(Scholarship, slug=slug)
    institution = scholarship.__getattribute__('instituicao')
    if not institution.checked and not institution.logged:
        return redirect("loginInstitution")

    if request.POST:
        scholarship.fotoPerfil.delete()
        scholarship.delete()
        messages.success(request, 'Bolsa deletada com sucesso!')
        return redirect("home")
    
    context['scholarship'] = scholarship
    return render(request, 'scholarship/deleteScholarship.html', context)

def listScholarships(request):
    context = {}
    
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')
    
    scholarships = Scholarship.objects.all()
    context['scholarships'] = scholarships
    return render(request,'scholarship/listScholarships.html', context)

def inscrever_scholarship(request, slug):
    scholarship = get_object_or_404(Scholarship, slug=slug)
    if request.method == 'POST':
        # Adicione aqui a lógica para inscrever o usuário na bolsa
        # Por exemplo, adicionar o usuário a uma lista de inscritos na bolsa
        return redirect('scholarship:view-scholarship', slug=scholarship.slug)
    return HttpResponse(status=405)  # Método não permitido se não for POST

def listar_scholarships_user(request):
    user_scholarships = Scholarship.objects.filter(inscritos=request.user)
    return render(request, 'scholarship/listScholarshipsUser.html', {'scholarships': user_scholarships})




