from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Zona(models.Model):
    sitio_dispositivo = models.CharField(max_length=20)
    coordenadas = models.CharField(max_length=20)

    def __str__(self):
        return self.sitio_dispositivo
    
class Dispositivo(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre