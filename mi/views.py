from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def padya(request):
    return HttpResponse('<h1>Captain of mi is padya</h1>')