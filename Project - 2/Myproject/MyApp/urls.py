from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('service/', views.service_view, name='service'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]


