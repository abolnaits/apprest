
from django.urls import path

from frontend import views

urlpatterns = [
   
   path('',views.front_list,name='front-list'),
    
]