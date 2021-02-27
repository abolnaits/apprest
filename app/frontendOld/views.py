from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def front_list(request):
    return render(request,'frontend/list.html')

