from django.urls import path
from institution import views

app_name ='institution'

urlpatterns = [
    path('<slug>/profile/', views.viewInstitution, name='profile-institution'),
    path('<slug>/edit/', views.editInstitution, name='edit-institution'),
    path('', views.listInstitutions, name='list-institution'),
    path('create/', views.createInstitution, name='create-institution'),
    path('<slug>/delete/', views.deleteInstitution, name='delete-institution'),
    path('institution/<slug:slug>/scholarships/', views.institutionScholarships, name='institution-scholarships'),

]