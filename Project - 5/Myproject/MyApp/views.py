from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'MyApp/home.html')

def qualification_view(request):
    context = {'qualification' : {
        'SSC':{'study':'SSC', 'Year':2016, 'Marks': 70, 'uni': 'MH'},
        'HSC':{'study':'HSC', 'Year':2018, 'Marks': 60, 'uni': 'MH'},
        'BSC':{'study':'BSCIT', 'Year':2021, 'Marks': 77, 'uni': 'Mumbai'}
    }}

    return render(request, 'MyApp/qualification.html', context)


def skills_view(request):
    context = {'skills': {
        'Core Python':70, 'Django Framework':60, 'HTML / CSS':50, 'JavaScript':60, 'JQuery':60, 'SQL':80, 'ReactJS':60 
    }}

    return render(request, 'MyApp/skills.html', context)


def projects_view(request):
    context = {'projects' : ['Project 1', 'Project 2', 'Project 3', 'Project 4', 'Project 5']}

    return render(request, 'MyApp/projects.html', context)


def experience_view(request):
    return render(request, 'MyApp/experience.html')

def contact_view(request):
    return render(request, 'MyApp/contact.html')

