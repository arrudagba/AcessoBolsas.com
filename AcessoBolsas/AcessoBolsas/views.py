from django.shortcuts import render
from django.views.generic import TemplateView

""" class HomeView(TemplateView):
    template = 'AcessoBolsas/index.html' """
    
    
def HomeView(request):
    context = {}
    
    return render(request, 'AcessoBolsas/index.html', context)