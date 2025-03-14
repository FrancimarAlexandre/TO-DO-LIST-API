from rest_framework import viewsets
from .serializers import ToDoListSerializer
from .models import ToDoList

# Create your views here.

class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    