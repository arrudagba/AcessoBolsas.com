from django.urls import path
from scholarship import views

app_name ='scholarship'

urlpatterns = [
    path('create/', views.createScholarship, name='create-scholarship'),
    path('<slug>/edit/', views.editScholarship, name='edit-scholarship'),
    # path('<slug>/', views.viewScholarship, name='view-scholarship'),
    path('<slug>/delete/', views.deleteScholarship, name='delete-scholarship'),
    path('list/', views.listScholarships, name='list-scholarship'),
]