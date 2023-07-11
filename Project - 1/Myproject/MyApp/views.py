from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    
    return HttpResponse('<h1>This is home page!</h1>')

def about_view(request):

    return HttpResponse('<h1>This is about page!</h1>')

def contact_view(request):

    return HttpResponse('<h1>This is contact page!</h1>')

def service_view(request):

    return HttpResponse('<h1>This is service page!')


