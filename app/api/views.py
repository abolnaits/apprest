from django.shortcuts import render

from django.http import JsonResponse

# Rest framework

from rest_framework.decorators import api_view
# Requerido para generar la respuesta de la API
from rest_framework.response import Response
# Serializer
from api.serializer import TaskSerializer
# Modelo
from api.models import Task

# Create your views here.

# Show all the URLS

@api_view(['GET'])
def api_over_view(request):
    api_urls={
        'List':'/task-list/',
        'Detail View':'/tast-detail/<str:pk>',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>'
    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    task = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(task,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    # Creo un objeto en la Tabla Task
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def task_update(request,pk):
    # Creo un objeto en la Tabla Task
    print('Update ==>',request)
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete(request,pk):
    # Creo un objeto en la Tabla Task
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task deleted')