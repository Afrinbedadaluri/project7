from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def one_one(request):
    return HttpResponse('<h1>one_one</h1>')

def one_two(request):
    return HttpResponse('<h1>one_two</h1>')
