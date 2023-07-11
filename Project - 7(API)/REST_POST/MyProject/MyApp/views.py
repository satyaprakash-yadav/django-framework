from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer

# Create your views here.

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        print(pythondata)
        serialize = StudentSerializer(data=pythondata)

        if serialize.is_valid():
            serialize.save()    
            response = {'msg':'Successfully added data'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        
