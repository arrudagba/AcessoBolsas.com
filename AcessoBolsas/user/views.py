from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from user.forms import UserRegisterForm, UserUpdateForm

# Create your views here.

def registerUser(request):
    context = {}

    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['registrationForm'] = form
    else:
        form = UserRegisterForm()
        context['registrationForm'] = form

    return render(request, 'user/registerUser.html', context)

def editUser(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    if request.POST:
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
                "name": request.POST['name'],
                "telefone": request.POST['telefone'],
                "dataNascimento": request.POST['dataNascimento'],
                "sexo": request.POST['sexo'],
            }
            form.save()
            messages.success(request, 'User atualizado com sucesso!')
        else:
            messages.warning(request, 'E-mail ou username indisponíveis. Tente novamente.')
    else:
        form = UserUpdateForm(
            {
                "email": request.user.email,
                "username": request.user.username,
                "name": request.user.name,
                "telefone": request.user.telefone,
                "dataNascimento": request.user.dataNascimento,
                "sexo": request.user.sexo,
            }
        )

    context['updateForm'] = form

    return render(request, 'user/editUser.html', context)

def deleteUser(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user:
            user.delete()
            messages.success(request, 'Usuário deletado com sucesso!')
            return redirect("home")
        else:
            messages.warning(request, 'Email ou senha incorretos! Tente novamente.')

    return render(request, 'user/deleteUser.html', context)

def viewUser(request):
    user = request.user
    context = {
        'username': user.username,
        'name': user.name,
        'email': user.email,
        'telefone': user.telefone,
        'dataNascimento': user.dataNascimento,
        'sexo': user.sexo,
        'foto_perfil': user.foto_perfil
    }
    return render(request, 'user/viewUser.html', context)


