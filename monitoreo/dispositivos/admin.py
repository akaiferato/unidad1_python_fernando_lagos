from django.contrib import admin
from .models import Categoria, Zona, Dispositivo, Medicion, Alerta

admin.site.register([Categoria, Zona, Medicion, Alerta])

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "estado", "categoria", "zona")
    list_filter = ("estado", "categoria")
    search_fields = ("nombre",)

