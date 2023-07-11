from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('qualification/', views.qualification_view, name='qualification'),
    path('skills/', views.skills_view, name='skills'),
    path('projects/', views.projects_view, name='projects'),
    path('experience/', views.experience_view, name='experience'),
    path('contact/', views.contact_view, name='contact')
]
