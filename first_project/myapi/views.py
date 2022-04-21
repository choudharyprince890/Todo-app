from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

# importing serializers and models
from myapi.serializer import TaskSerializer
from todo.models import Task

# Create your views here.
@api_view(['GET'])
def taskDetail(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    print("user",request.data)
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=HTTP_200_OK)
    else:
        return Response(serializer.errors)


@api_view(['DELETE'])
def deleteTask(request, pk):
    print("pk",pk)
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response('Task is deleted')



# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#     def create(self, request, *args, **kwargs):
#         return Response({'Test':"added sucessfully"},status=HTTP_200_OK)


