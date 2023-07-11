from django.urls import path
from . import views

urlpatterns = [
    #  path(raout, view_function, pathname)
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/',views.contact_view, name='contact'),
    path('service/', views.service_view, name='service'),
]



