from rest_framework import serializers
from .models import Vehiculo, Cliente, Inspeccion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class VehiculoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()  
    
    class Meta:
        model = Vehiculo
        fields = ['id', 'vin', 'marca', 'modelo', 'año', 'placa', 'servicio', 'comentario', 'cliente']
    
    def create(self, validated_data):
        # Extraer datos del cliente
        cliente_data = validated_data.pop('cliente')
        
        # Crear el cliente primero
        cliente = Cliente.objects.create(**cliente_data)
        
        # Crear el vehículo con el cliente creado
        vehiculo = Vehiculo.objects.create(cliente=cliente, **validated_data)
        
        return vehiculo
    
        

class InspeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspeccion
        fields = "__all__"