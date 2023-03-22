from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ToDoList(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    date = models.DateTimeField("date published", default=timezone.now())
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=500)
    toDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
