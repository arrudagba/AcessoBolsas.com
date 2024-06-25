from django.shortcuts import render
from django.views.generic import TemplateView
from scholarship.models import Scholarship
from operator import attrgetter

""" class HomeView(TemplateView):
    template = 'AcessoBolsas/index.html' """
    
    
def HomeView(request):
    context = {}
    scholarship = sorted(Scholarship.objects.all(), key=attrgetter('titulo'), reverse=True)
    context['scholarships'] = scholarship
    return render(request, 'AcessoBolsas/index.html', context)

def SignUp(request):
    context = {}
    
    return render(request, 'AcessoBolsas/decisaoCadastro.html', context)

def SignIn(request):
    context = {}

    return render(request, 'AcessoBolsas/decisaoLogin.html', context)

