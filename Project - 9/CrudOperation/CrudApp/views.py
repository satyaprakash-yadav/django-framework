from django.shortcuts import render, redirect
from .models import Employees

# Create your views here.

def home_view(request):
    emp = Employees.objects.all()

    context = {'emp':emp}
    return render(request, 'CrudApp/index.html',context)

def add_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone
        )

        emp.save()
        return redirect('home')
    
    return render(request, 'CrudApp/index.html')
    

def edit_view(request):
    emp = Employees.objects.all()
    context = {'emp':emp}
    return render(request, 'CrudApp/index.html', context)

def update_view(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )

        emp.save()
        return redirect('home')

    return render(request, 'CrudApp/index.html')


def delete_view(request, id):
    emp = Employees.objects.filter(id=id)
    emp.delete()
    return redirect('home')

def deleteAll_view(request):
    emp = Employees.objects.all()
    emp.delete()
    return redirect('home')

