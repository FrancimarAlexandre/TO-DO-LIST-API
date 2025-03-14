from django.db import models

# Create your models here.

class ToDoList(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    finish_at = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'tarefa:{self.title}'
    
    