from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'MyApp/home.html')

def contact_view(request):
    return render(request, 'MyApp/contact.html')

def about_view(request):
    return render(request, 'MyApp/about.html')

def service_view(request):
    return render(request, 'MyApp/service.html')

