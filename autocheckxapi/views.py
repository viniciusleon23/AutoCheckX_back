from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VehiculoSerializer,InspeccionSerializer,ClienteSerializer
from .models import Vehiculo,Cliente,Inspeccion
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class VehiculoView(viewsets.ModelViewSet):
    serializer_class = VehiculoSerializer
    queryset = Vehiculo.objects.all()
    @action(detail=False, methods=['get'], url_path='pendientes')
    def pendientes(self, request):
        """
        Obtener vehículos con inspección pendiente
        URL: /api/v1/vehiculos/pendientes/
        """
        vehiculos_pendientes = Vehiculo.objects.filter(
            inspeccion__estatus='Pendiente'
        ).distinct()
        
        serializer = self.get_serializer(vehiculos_pendientes, many=True)
        return Response({
            'count': vehiculos_pendientes.count(),
            'results': serializer.data
        })
    
    @action(detail=False, methods=['get'], url_path='realizados')
    def realizados(self, request):
        """
        Obtener vehículos con inspección realizada
        URL: /api/v1/vehiculos/realizados/
        """
        vehiculos_realizados = Vehiculo.objects.filter(
            inspeccion__estatus='Realizado'
        ).distinct()
        
        serializer = self.get_serializer(vehiculos_realizados, many=True)
        return Response({
            'count': vehiculos_realizados.count(),
            'results': serializer.data
        })
        
        
    
    
    
    
    
class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    
    
class InspeccionView(viewsets.ModelViewSet):
    serializer_class = InspeccionSerializer
    queryset = Inspeccion.objects.all()
    
    
    
    
