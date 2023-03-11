from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def two_one(request):
    return HttpResponse('<h1>two_one</h1>')
def two_two(request):
    return HttpResponse('<h1>two_two</h1>')


