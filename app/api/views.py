from django.shortcuts import render

from django.http import JsonResponse

# Rest framework
# Decorator for views
from rest_framework.decorators import api_view
# Requerido para generar la respuesta de la API
from rest_framework.response import Response
# Serializer
# Basicamente es retornar un objecto tipo Model como 
# un objeto tipo JSON response
from api.serializer import TaskSerializer
# Modelo
from api.models import Task

# Create your views here.

# Show all the URLS
# Entry point to the API app
# We must define the type of the VIEW in this case GET
@api_view(['GET'])
def api_over_view(request):
    api_urls={
        'List':'/task-list/',
        'Detail View':'/tast-detail/<str:pk>',
        'Add':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>'
    }
    return Response(api_urls)

# List all the task in the DB
@api_view(['GET'])
def task_list(request):
    # Get all the tasks
    task = Task.objects.all().order_by('-id')
    # Serialize all the tasks many = all the list
    serializer = TaskSerializer(task,many=True)
    # Return serialized data
    return Response(serializer.data)

# Show the detail for one specific item
@api_view(['GET'])
def task_detail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)

#Create a new task and save it in the DB
@api_view(['POST'])
def task_create(request):
    # Creo un objeto en la Tabla Task
    # data = POST enviado 
    serializer = TaskSerializer(data=request.data)
    # Valido los datos pasados al serializer
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Update a task based on the PK
@api_view(['POST'])
def task_update(request,pk):
    # Creo un objeto en la Tabla Task
    print('Update ==>')
    task = Task.objects.get(id=pk)
    # Obtengo la instancia que sera la task con ese PK
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete a task based on the PK
@api_view(['DELETE'])
def task_delete(request,pk):
    # Obtengo un objeto de la Tabla Task
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task deleted')