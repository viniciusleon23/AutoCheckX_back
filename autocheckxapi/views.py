from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VehiculoSerializer,InspeccionSerializer,ClienteSerializer
from .models import Vehiculo,Cliente,Inspeccion
# Create your views here.

class VehiculoView(viewsets.ModelViewSet):
    serializer_class = VehiculoSerializer
    queryset = Vehiculo.objects.all()
    
    
    
    
class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    
    
class InspeccionView(viewsets.ModelViewSet):
    serializer_class = InspeccionSerializer
    queryset = Inspeccion.objects.all()
    
    
    
    
