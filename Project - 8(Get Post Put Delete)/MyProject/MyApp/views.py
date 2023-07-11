from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
@csrf_exempt
def studentapi_view(request):
    
    # GET Method
    if request.method == 'GET':
        all_data = StudentModel.objects.all()
        serialize = StudentSerializer(all_data, many=True)
        json_data = JSONRenderer().render(serialize.data)

        return HttpResponse(json_data, content_type='application/json')
    

    # POST Method
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)    
        python_data = JSONParser().parse(stream)
        serialize = StudentSerializer(data=python_data)
        if serialize.is_valid():
            serialize.save()
            response = {'msg': 'Data Successfully Save'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serialize.errors)
        return HttpResponse(json_data, 'application/json')
    

    # PUT Method
    if request.method == "PUT":
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        sid = StudentModel.objects.get(id=id)
        serialize = StudentSerializer(sid, data=python_data, partial=True)
        if serialize.is_valid():
            serialize.save()
            response = {'msg':'Data Successfully Updated'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        

    # DELETE Method
    if request.method == 'DELETE':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)

        if id is not None:
            data = StudentModel.objects.get(id=id)
            data.delete()
            json_data = {'msg': 'Data Successfully Remove'}
            response = JSONRenderer().render(json_data)
            return HttpResponse(response, content_type='application/json')
        
        json_data = {'msg': 'Id Not Provided'}
        response = JSONRenderer().render(json_data)

        return HttpResponse(response, content_type='application/json')
    

    



