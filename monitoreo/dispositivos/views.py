from django.shortcuts import render
from django.http import HttpResponse
from .models import Dispositivo, Medicion

def index(request):
    mediciones = Medicion.objects.select_related("dispositivo")
    context = {"mediciones" : mediciones}
    return render(request, "dispositivos/index.html", context)

def dispositivo(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)
    context = {"dispositivo" : dispositivo}

    return render(request, "dispositivos/dispositivo.html", context)
