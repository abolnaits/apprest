from rest_framework import serializers
from api.models import Task

# Modelo a ser serializado
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Modelo
        model = Task
        # Que campos vamos a mostrar
        fields='__all__'
