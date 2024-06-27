"""
URL configuration for AcessoBolsas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from AcessoBolsas.views import HomeView
from AcessoBolsas.views import SignUp
from AcessoBolsas.views import SignIn
from user.views import (
    loginUser,
    logoutUser,
    registerUser,
    myAccountUser,
)
from institution.views import (
    loginInstitution,
    logoutInstitution,
    createInstitution,
    myAccountInstitution,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView , name='home'),
    path('user/', include('user.urls')),
    path('<username>/my_account/', myAccountUser, name='my_account'),
    path('<slugInstitution>/my_account_institution/', myAccountInstitution, name='my_account_institution'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('loginInstitution/', loginInstitution, name='loginInstitution'),
    path('logoutInstitution/', logoutInstitution, name='logoutInstitution'),
    path('scholarship/', include('scholarship.urls')),
    path('institution/', include('institution.urls')),
    path('sign_in/', SignIn, name='sign_in'),
    path('sign_up/', SignUp, name='sign_up'),
    path('sign_up/institution/', createInstitution, name='sign_up_institution'),
    path('sign_up/user/', registerUser, name='sign_up_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)