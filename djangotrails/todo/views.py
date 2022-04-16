from django.shortcuts import render,HttpResponse
from .models import Todo

# Create your views here.
def index(request):
    return HttpResponse(Todo.objects.all())