from django.db import models

class Medicion:
    consumo = models.IntegerField()
    fecha = models.DateField()
    limite_consumo = models.IntegerField()
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    
    def __str__():
        return self.consumo

class Alerta:
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    medicion = models.OneToOneField(Medicion, on_delete=models.CASCADE)

    def __str__():
        return nombre


