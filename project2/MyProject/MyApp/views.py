from django.shortcuts import render , HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse('Home Page')

def service_view(request):
    return HttpResponse('Service Page')

def about_view(request):
    return HttpResponse('About Page')

def contact_view(request):
    return HttpResponse('Contact Page')
