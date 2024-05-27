from django.urls import path
from institution import views

app_name ='institution'

urlpatterns = [
    path('<slug>/profile/', views.perfil_instituicao, name='profile-institution'),
    path('<slug>/edit/', views.editar_perfil, name='edit-institution'),
    path('', views.listInstitutions, name='list-institution'),
]