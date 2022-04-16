from asyncio.windows_events import NULL
from pickle import TRUE
from pyexpat import model
from tabnanny import verbose
from django.db import models


class Author(models.Model):
    a_name = models.CharField(max_length=75)
    a_designation = models.CharField(max_length=75,choices=models.TextChoices('designation', 'Trainee Employee Manager CEO').choices,default='Trainee')
    a_exp = models.IntegerField()

    def __str__(self) -> str:
        return self.a_name
    class Meta:
        verbose_name_plural = "Author's"
        
class Todo(models.Model): 
    todo_auth = models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    todo_title = models.CharField(max_length=100)
    todo_desc = models.TextField(max_length=100)
    tag_name = models.CharField(max_length=100,choices=models.TextChoices('TagName', 'Important Urgent Top').choices,default='NA')
    status_name = models.CharField(max_length=100,choices=models.TextChoices('StatusName', 'ToDo InProgress InReview Done').choices,default='NA')

    def __str__(self) -> str:
        return self.todo_title
    class Meta:
        verbose_name_plural = "Todo's"
    
