from rest_framework import serializers
from django.db import transaction
from .models import Vehiculo, Cliente, Inspeccion
import logging
from datetime import date

logger = logging.getLogger(__name__)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        

class InspeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspeccion
        fields = ["marca","fecha_servicio","vehiculo","luces_frontales","luces_posteriores","carga_bateria","presion_llanta_uno","presion_llanta_dos","presion_llanta_tres","presion_llanta_cuatro","estatus"]

class VehiculoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()  
    
    class Meta:
        model = Vehiculo
        fields = ['id', 'vin', 'marca', 'modelo', 'año', 'placa', 'servicio', 'comentario','fecha_registro', 'cliente']
        
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            # Extraer datos del cliente
            cliente_data = validated_data.pop('cliente')
            
            # Crear el cliente primero
            cliente = Cliente.objects.create(**cliente_data)
            logger.info(f"Cliente creado: {cliente.id} - {cliente.nombre}")
            
            # Crear el vehículo con el cliente creado
            vehiculo = Vehiculo.objects.create(cliente=cliente, **validated_data)
            logger.info(f"Vehículo creado: {vehiculo.id} - {vehiculo.vin}")
            
            # Crear automáticamente una inspección pendiente para el vehículo
            inspeccion = Inspeccion.objects.create(
                vehiculo=vehiculo,
                marca=vehiculo.marca, 
                fecha_servicio=None,  
                estatus="Pendiente",
                luces_frontales=None,
                luces_posteriores=None,
                carga_bateria=None,
                presion_llanta_uno=None,
                presion_llanta_dos=None,
                presion_llanta_tres=None,
                presion_llanta_cuatro=None
            )
            logger.info(f"Inspección creada automáticamente: {inspeccion.id} - Estatus: {inspeccion.estatus}")
            
            return vehiculo
            
        except Exception as e:
            logger.error(f"Error al crear vehículo y/o inspección: {str(e)}")
            raise serializers.ValidationError(
                f"Error al crear el registro: {str(e)}"
            )
            
            
class VehiculoConInspeccionSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    inspeccion_id = serializers.SerializerMethodField()
    inspeccion_estatus = serializers.SerializerMethodField()
    
    class Meta:
        model = Vehiculo
        fields = ['id', 'vin', 'marca', 'modelo', 'año', 'placa', 'servicio', 'comentario','fecha_registro', 'cliente', 'inspeccion_id', 'inspeccion_estatus']
    
    def get_inspeccion_id(self, obj):
        try:
            inspeccion = Inspeccion.objects.get(vehiculo=obj)
            return inspeccion.id
        except Inspeccion.DoesNotExist:
            return None
    
    def get_inspeccion_estatus(self, obj):
        try:
            inspeccion = Inspeccion.objects.get(vehiculo=obj)
            return inspeccion.estatus
        except Inspeccion.DoesNotExist:
            return None