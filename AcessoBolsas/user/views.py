from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from user.models import User
from user.forms import UserRegisterForm, UserUpdateForm, UserAuthForm
from institution.models import Institution

# Create your views here.

@csrf_protect
def registerUser(request):
    context = {}

    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

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

    user = get_object_or_404(User, slug=slug)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User atualizado com sucesso!')
            return redirect('home')
        else:
            messages.warning(request, 'E-mail ou username indisponíveis. Tente novamente.')
    else:
        form = UserUpdateForm(instance=user)

    context = {'updateForm': form}

    return render(request, 'user/editUser.html', context)

def deleteUser(request, slug):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password, slug=slug)

        if user:
            user.delete()
            logout(request)
            messages.success(request, 'Usuário deletado com sucesso!')
            return redirect("home")
        else:
            messages.warning(request, 'Username ou senha incorretos! Tente novamente.')

    return render(request, 'user/deleteUser.html', context)

def viewUser(request, slug):
    context = {}

    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

    user = get_object_or_404(User, slug=slug)
    context['user'] = user
    return render(request, 'user/viewUser.html', context)

def listUsers(request):
    context = {}

    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

    users = User.objects.all()
    context['users'] = users
    return render(request,'user/listUsers.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logout feito com sucesso!')
    return redirect("home")

def loginUser(request):
    context = {}

    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')

    response = redirect('home')
    if request.COOKIES.get('logged') == True:
        institution = Institution.objects.get(slug=request.COOKIES.get('slugInstitution'))
        institution.logged = False
        response.set_cookie('logged', False)
        response.set_cookie('slugInstitution', None)
        response.set_cookie('nameInstitution', None)
        institution.save()
        
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    
    if request.method == 'POST':
        form = UserAuthForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Login feito com sucesso!')
                return response
    
    else:
        form = UserAuthForm()

    context['loginForm'] = form
    return render(request, 'user/loginUser.html', context)

def myAccountUser(request, username):
    context = {}
    context['slugInstitution'] = request.COOKIES.get('slugInstitution')
    context['nameInstitution'] = request.COOKIES.get('nameInstitution')
    context['institutionLogged'] = request.COOKIES.get('logged')
    
    user = get_object_or_404(User, username=username)
    context['user'] = user
    return render(request,'user/viewUser.html', context)