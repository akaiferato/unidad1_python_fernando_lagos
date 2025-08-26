from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
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
