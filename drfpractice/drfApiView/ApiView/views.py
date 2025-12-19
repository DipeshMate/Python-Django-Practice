from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import StudentDetail
from .serializers import StudentSerializer
from rest_framework import status


@api_view(['GET','POST','PUT','DELETE']) # browsable-api for api testing
def Home(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = StudentDetail.objects.get(pk=id)
            serialize = StudentSerializer(stu)
            return Response({'msg':'Get request Created','data':serialize.data}) 
        stu = StudentDetail.objects.all()
        serialize = StudentSerializer(stu, many=True)
        return Response({'msg':'Get request Created','data':serialize.data}) 
    
    if request.method == 'POST':
        # print('Post Added Data:',request.data)
        serialize = StudentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg':'Post request Created and Added New Student', 'data':serialize.data}, status=status.HTTP_201_CREATED)
        return Response(serialize.errors)
    
    if request.method == 'PUT':
        stu = StudentDetail.objects.get(id=request.data.get('id'))
        serialize = StudentSerializer(stu, data=request.data,partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg':'PUT Data Updated!!'})
        return Response(serialize.errors)
    
    if request.method == 'DELETE':
        stu = StudentDetail.objects.get(id=request.data.get('id'))
        stu.delete()
        return Response({'msg':'DELETE Request Data Deleted!!'})
        