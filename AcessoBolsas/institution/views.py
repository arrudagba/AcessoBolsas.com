from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from institution.models import Institution

@login_required
def perfil_instituicao(request):
    perfil = Institution.objects.get(usuario=request.user)
    return render(request, 'perfil_instituicao.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil = Institution.objects.get(usuario=request.user)

    if request.method == 'POST':
        perfil.nome = request.POST['nome']
        perfil.cnpj = request.POST['cnpj']
        perfil.contato = request.POST['contato']
        perfil.endereco = request.POST['endereco']
        perfil.descricao = request.POST['descricao']
        if 'foto_perfil' in request.FILES:
            perfil.foto_perfil = request.FILES['foto_perfil']
        perfil.save()
        return redirect('perfil_instituicao')

    return render(request, 'editar_perfil.html', {'perfil': perfil})


def listInstitutions(request):
    context = {}
    institutions = Institution.objects.all()
    context['institutions'] = institutions
    return render(request,'institution/listInstitutions.html', context)
