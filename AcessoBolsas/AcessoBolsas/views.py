from django.shortcuts import render
from django.views.generic import TemplateView

""" class HomeView(TemplateView):
    template = 'AcessoBolsas/index.html' """
    
    
def HomeView(request):
    context = {}
    
    return render(request, 'AcessoBolsas/index.html', context)

def SignUp(request):
    context = {}
    
    return render(request, 'AcessoBolsas/decisaoCadastro.html', context)

def SignUpInstitution(request):
    context = {}
    
    return render(request, 'AcessoBolsas/cadastroInst.html', context)

def SignUpUser(request):
    context = {}
    
    return render(request, 'AcessoBolsas/cadastroUsuario.html', context)

