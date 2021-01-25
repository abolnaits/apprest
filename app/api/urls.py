from django.urls import path
from api import views



urlpatterns = [
    path('',views.api_over_view,name='api-overview'),
    path('task-list/',views.task_list,name='api-task-list'),
    path('task-detail/<str:pk>',views.task_detail,name='api-task-detail'),
    path('task-create/',views.task_create,name='api-task-create'),
    path('task-update/<str:pk>',views.task_update,name='api-task-update'),
    path('task-delete/<str:pk>',views.task_delete,name='api-task-delete'),
           
]
