from django.shortcuts import render , HttpResponse

# Create your views here.

def home_view(request):

    return HttpResponse("<h1>This is Home Page!</h1>")

def about_view(request):

    return HttpResponse("<h1>This is About Page1</h1>")

def contact_view(request):

    return HttpResponse("<h1>This is Contact Page1</h1>")
    