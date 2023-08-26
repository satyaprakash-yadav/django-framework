from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'), 
    path('create-record', views.create_record, name="create-record"),
    path('vote/<int:pk>/', views.vote, name='vote'),
    path('result/<int:pk>/', views.result, name='result'),
    path('logout/', views.logout, name='logout'),
]
