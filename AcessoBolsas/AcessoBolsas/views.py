from django.shortcuts import render

def viewHome(request):
    context = {}
    return render(request, 'index.html', context)