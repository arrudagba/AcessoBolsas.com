from django.shortcuts import render, redirect, get_object_or_404
from scholarship.forms import ScholarshipRegisterForm, ScholarshipUpdateForm
from django.contrib import messages
from institution.models import Institution
from scholarship.models import Scholarship

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