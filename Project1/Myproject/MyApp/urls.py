from django.urls import path
from .import views

urlpatterns = [
    #path(rout , view_function , pathname)
    path('' , views.home_view , name="name"),
    path('about/' , views.about_view , name="about"),
    path('contact/' , views.contact_view , name="contact"),
]
