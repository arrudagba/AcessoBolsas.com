from django.shortcuts import render
from django.views.generic import TemplateView
from scholarship.models import Scholarship
from django.http import HttpResponse
from operator import attrgetter

""" class HomeView(TemplateView):
    template = 'AcessoBolsas/index.html' """
    
    
def HomeView(request):
    context = {}
    query = request.GET.get('q')
    if query:
        scholarships = Scholarship.objects.filter(titulo__icontains=query)
    else:
        scholarships = sorted(Scholarship.objects.all(), key=attrgetter('titulo'), reverse=True)
    
    institutionLogged = request.COOKIES.get('logged')
    if institutionLogged is None:
        context['institutionLogged'] = None
        print("institutionLogged = None")
    else:
        if institutionLogged == 'True':
            context['institutionLogged'] = True
            context['slugInstitution'] = request.COOKIES.get('slugInstitution')
            context['nameInstitution'] = request.COOKIES.get('nameInstitution')
            print("institutionLogged = True")
        else:
            context['institutionLogged'] = False
            print("institutionLogged = False")
    context['scholarships'] = scholarships
    
    return render(request, 'AcessoBolsas/index.html', context)

def SignUp(request):
    context = {}
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')
    
    return render(request, 'AcessoBolsas/decisaoCadastro.html', context)

def SignIn(request):
    context = {}
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

    return render(request, 'AcessoBolsas/decisaoLogin.html', context)

