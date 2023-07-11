from django.shortcuts import render

# Create your views here.

def home_view(request):
    context = {'course': 'Django', 'loc': 'Thane'}

    try:
        if request.method == 'POST':
            num = int(request.POST['number'])
            print(num)
            context['num'] = num

    except:
        context['num'] = None

    return render(request, 'MyApp/home.html', context)


def service_view(request):
    context = {'services':['Python', 'Java', 'Dot Net', 'Testing']}

    return render(request, 'MyApp/service.html', context)
    

def category_view(request):
    context = {'python':{'core': 'Basic Python', 'advance': 'Django'}}

    return render(request, 'MyApp/category.html', context)


