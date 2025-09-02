from django.db import models
from django.utils import timezone

# Clase base con atributos comunes

class BaseModel(models.Model):
    ESTADOS = [
            ("ACTIVO", "activo"),
            ("INACTIVO", "inactivo")
            ]

    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Categoria(BaseModel):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Zona(BaseModel):
    sitio_dispositivo = models.CharField(max_length=20)
    coordenadas = models.CharField(max_length=20)

    def __str__(self):
        return self.sitio_dispositivo

class Dispositivo(BaseModel):
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Medicion(BaseModel):
    consumo = models.IntegerField()
    fecha = models.DateField()
    limite_consumo = models.IntegerField()
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.consumo)

class Alerta(BaseModel):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    medicion = models.OneToOneField(Medicion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
