from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from user.models import User
from user.forms import UserRegisterForm, UserUpdateForm

# Create your views here.

def registerUser(request):
    context = {}

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Usuário cadastrado com sucesso!')
                return redirect('home')
            else:
                messages.error(request, 'Erro ao cadastrar usuário!')
                return redirect('login')
        else:
            context['registrationForm'] = form
    else:
        form = UserRegisterForm()
        context['registrationForm'] = form

    return render(request, 'user/registerUser.html', context)

def editUser(request, slug):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    user = get_object_or_404(User, slug=slug)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user, slug=slug)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
                "nome": request.POST['nome'],
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
                "email": user.email,
                "username": user.username,
                "nome": user.nome,
                "telefone": user.telefone,
                "dataNascimento": user.dataNascimento,
                "sexo": user.sexo,
            }
        )

    context['updateForm'] = form

    return render(request, 'user/editUser.html', context)

def deleteUser(request, slug):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password, slug=slug)

        if user:
            user.delete()
            messages.success(request, 'Usuário deletado com sucesso!')
            return redirect("home")
        else:
            messages.warning(request, 'Username ou senha incorretos! Tente novamente.')

    return render(request, 'user/deleteUser.html', context)

def viewUser(request, slug):
    context = {}
    user = get_object_or_404(User, slug=slug)
    context['user'] = user
    return render(request, 'user/viewUser.html', context)

def listUsers(request):
    context = {}
    users = User.objects.all()
    context['users'] = users
    return render(request,'user/listUsers.html', context)
