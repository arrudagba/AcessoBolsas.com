from django.urls import path
from institution import views

app_name ='institution'

urlpatterns = [
    path('<slug>/edit/', views.editar_perfil, name='edit-institution'),
]