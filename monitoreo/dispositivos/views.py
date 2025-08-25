from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    context = {}
    return render(request, "dispositivos/index.html")
