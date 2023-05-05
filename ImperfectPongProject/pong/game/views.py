from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

def instructions(request):
    return render(request,'instructions.html')

def game(request):
    return render(request, 'BasicPong.html')