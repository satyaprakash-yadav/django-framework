from django.shortcuts import render, HttpResponse
from . models import StudentModel
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

def get_data_view(request, id):
    data = StudentModel.objects.get(id=id)
    python_data = StudentSerializer(data)
    print(python_data.data)

    jsondata = JSONRenderer().render(python_data.data)
    return HttpResponse(jsondata, content_type='application/json')

def all_data_view(request):
    data = StudentModel.objects.all()
    python_data = StudentSerializer(data, many=True)
    print(python_data.data)

    jsondata = JSONRenderer().render(python_data.data)
    return HttpResponse(jsondata, content_type='application/json')

