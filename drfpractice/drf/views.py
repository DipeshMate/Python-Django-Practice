from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentDetail
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt

def Home(request):
    st = StudentDetail.objects.all()
    print('St:',st)
    serializer = StudentSerializer(data = st, many= True)
    print('Serializer',serializer)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def studentInfo(request,id):
    st = StudentDetail.objects.get(pk=id)
    context= {'st':(st)}
    return render(request,'Home.Html',{'st':context})

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            json_data = request.body # request.body or form Data
            print('json_data:',json_data) #json_data
            stream = io.BytesIO(json_data)
            print('Stream',stream)
            python_data = JSONParser().parse(stream)
            print('Python_Data:', python_data)
            
            # Serialize the data
            serializer = StudentSerializer(data = python_data) # serializer
            print('Serializer:',serializer)
            if serializer.is_valid():
                serializer.save()
                res_2_cli = {'msg':'Data Created'}
                jsonData = JSONRenderer().render(res_2_cli)
                print('jsonData:',jsonData)
                return HttpResponse(jsonData,content_type='application/json')
            
            else:
                # Return errors if the serializer is not valid
                jsonData = JSONRenderer().render(serializer.errors)
                return HttpResponse(jsonData, content_type='application/json', status=400)
        except Exception as e:
            # Handle any unexpected errors
            error_message = {'msg': str(e)}
            jsonData = JSONRenderer().render(error_message)
            return HttpResponse(jsonData, content_type='application/json', status=500)
    return HttpResponse('Method Not Allowed', status=405)