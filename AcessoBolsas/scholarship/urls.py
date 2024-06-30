from django.urls import path
from scholarship import views

app_name = 'scholarship'

urlpatterns = [
    path('create/', views.createScholarship, name='create-scholarship'),
    path('<slug>/edit/', views.editScholarship, name='edit-scholarship'),
    path('<slug>/profile/', views.viewScholarship, name='profile-scholarship'),
    path('<slug>/delete/', views.deleteScholarship, name='delete-scholarship'),
    path('inscricoes/', views.listar_scholarships_user, name='listar-scholarships-user'),  # Colocando antes do path com slug
    path('', views.listScholarships, name='list-scholarship'),
    path('<slug>/', views.viewScholarship, name='view-scholarship'),
    path('inscrever/<slug>/', views.inscrever_scholarship, name='inscrever-scholarship'),
]
