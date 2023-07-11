from django.shortcuts import render, redirect
from .forms import RegisterForm, ImageForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import CategoryModel, ImageModel

# Create your views here.

def home_view(request):
    # if request.user.is_authenticated is False:
    #     return redirect('gallery')
    return render(request, 'GalleryApp/home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User register Successfully...')
            return redirect('login')
    
    else:
        form = RegisterForm
    context = {'form' : form}
    return render(request, 'GalleryApp/register.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, 'User Login Successfully...')
            return redirect('gallery')

        else:
            messages.warning(request, 'something went wrong')   
    return render(request, 'GalleryApp/login.html')


def gallery_view(request):
    categories = CategoryModel.objects.all()
    Images = ImageModel.objects.all()
    context = {'categories':categories, 'Images':Images}
    return render(request, 'GalleryApp/gallery.html', context)


def category_view(request, id):
    categories = CategoryModel.objects.all()
    cat = CategoryModel.objects.get(id = id)
    Images = ImageModel.objects.filter(Category=cat)
    context = {'categories':categories, 'Images':Images}
    return render(request, 'GalleryApp/gallery.html', context)


def logout_view(request):
    logout(request)
    messages.warning(request, 'User Logout Successfully...')
    return redirect('home')


def add_view(request):
    forms = ImageForm()
    if request.method == 'POST':
        forms = ImageForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Image Uploaded SuccessFully...')
            return redirect('gallery')
        
    context = {'forms': forms}
    return render(request, 'GalleryApp/add.html', context)

