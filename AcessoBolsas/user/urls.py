from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.registerUser, name='register-user'),
    path('<slug>/edit/', views.editUser, name='edit-user'),
    path('<slug>/delete/', views.deleteUser, name='delete-user'),
    path('<slug>/profile/', views.viewUser, name='profile-user'),
    path('', views.listUsers, name='list-user'),
]