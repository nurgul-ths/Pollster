from django.shortcuts import render

from .models import Question, Choice

def index(request):
    return render(request, 'polls/index.html')