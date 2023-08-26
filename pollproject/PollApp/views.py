from django.shortcuts import render, redirect
from . models import PollRecord
from . forms import CreateRecordForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import auth
from . models import PollRecord, Vote

# Create your views here.

def home(request):
    records = PollRecord.objects.all()
    context = {"records": records}
    return render(request, "PollApp/home.html", context=context)



def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.cleaned_data.get['username']
            # messages.success(request, "Account was created for " + user)

            return redirect("login")

    context = {'form': form}
    return render(request, 'PollApp/register.html', context)



def login(request):
    if request.method == "POST":
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.info(request, "Username OR password is incorrect")
            
    return render(request, 'PollApp/login.html')



def create_record(request):
    form = CreateRecordForm()
    
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was created!")
            return redirect("home")
    context = {"form": form}
    return render(request, "PollApp/create-record.html", context=context)


def vote(request, pk):
    records = PollRecord.objects.get(id=pk)
    return render(request, 'PollApp/vote.html', {'records':records})


def result(request, pk):
    records = PollRecord.objects.get(id=pk)
    vote = Vote.objects.all()
    if request.method == 'POST':
        value = request.POST['choice']
        selection_option = vote.get(id=value)
        selection_option.vote += 1
        selection_option.save()
    # Vote.objects.all().update(vote=value)
    return render(request, 'PollApp/result.html', {'records':records, 'votes': vote})

def logout(request):
    auth.logout(request)
    return redirect('login')


