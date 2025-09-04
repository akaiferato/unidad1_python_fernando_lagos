from django.shortcuts import render
from django.http import HttpResponse
from .models import Dispositivo

def index(request):
    dispositivos = [
            {"nombre" : "Sensor Temperatura", "consumo" : 50},
            {"nombre" : "Medidor Solar", "consumo" : 120},
            {"nombre" : "Sensor Movimiento", "consumo" : 30},
            {"nombre" : "Calefactor", "consumo" : 200}
        ]
    consumo_maximo = 100
    context = {"dispositivos" : dispositivos,
               "consumo_maximo" : consumo_maximo}

    return render(request, "dispositivos/index.html", context)

def dispositivo(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)
    context = {"dispositivo" : dispositivo}

    return render(request, "dispositivos/index.html", context)
