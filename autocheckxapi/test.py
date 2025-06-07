from django.db import models

# Declaración de la tabla clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=50)  
    
    def __str__(self):
        return self.nombre 


class Vehiculo(models.Model):
    vin = models.CharField(max_length=17)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año = models.IntegerField()  # Sin max_length
    placa = models.CharField(max_length=7)
    servicio = models.CharField(max_length=200)
    comentario = models.CharField(max_length=200)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"
    
    
    
class Inspeccion(models.Model):
    MARCAS_CHOICES = [
        ('nissan', 'Nissan'),
        ('hyundai', 'Hyundai'),
        ('mazda', 'Mazda'),
    ]
    
    marca = models.CharField(max_length=20, choices=MARCAS_CHOICES)
    fecha_servicio = models.DateField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    
    # Campos comunes
    luces_frontales = models.CharField(max_length=20, blank=True, null=True)
    luces_posteriores = models.CharField(max_length=20, blank=True, null=True)
    carga_bateria = models.IntegerField(blank=True, null=True)
    
    # Campos específicos para llantas
    presion_llanta_uno = models.FloatField(blank=True, null=True)
    presion_llanta_dos = models.FloatField(blank=True, null=True)
    presion_llanta_tres = models.FloatField(blank=True, null=True)
    presion_llanta_cuatro = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return f"Inspección {self.marca} - {self.vehiculo.placa}"
    
    
    