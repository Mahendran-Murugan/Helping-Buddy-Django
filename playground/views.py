from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# request handler

def sayHello(request):
    return render(request, 'hello.html')