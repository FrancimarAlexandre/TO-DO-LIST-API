from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ToDoListViewSet

router = DefaultRouter()

router.register(r'ToDoList',ToDoListViewSet,basename='ToDoList')

urlpatterns = [
    path("",include(router.urls)),
]
