from django.shortcuts import render
from django.views.generic import TemplateView
from scholarship.models import Scholarship
from django.http import HttpResponse
from operator import attrgetter

""" class HomeView(TemplateView):
    template = 'AcessoBolsas/index.html' """
    
    
def HomeView(request):
    query = request.GET.get('q')
    if query:
        scholarships = Scholarship.objects.filter(titulo__icontains=query)
    else:
        scholarships = sorted(Scholarship.objects.all(), key=attrgetter('titulo'), reverse=True)
    
    institutionLogged = request.COOKIES.get('logged')
    context = {
        'scholarships': scholarships,
        'institutionLogged': institutionLogged == 'True' if institutionLogged else None
    }

    return render(request, 'AcessoBolsas/index.html', context)

def SignUp(request):
    context = {}
    
    return render(request, 'AcessoBolsas/decisaoCadastro.html', context)

def SignIn(request):
    context = {}

    return render(request, 'AcessoBolsas/decisaoLogin.html', context)

