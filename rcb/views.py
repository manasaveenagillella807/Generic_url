from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h1>Captain of rcb is virat Kohili</h1>')