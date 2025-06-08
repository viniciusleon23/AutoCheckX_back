
from django.urls import include, path
from rest_framework import routers
from autocheckxapi import views

router = routers.DefaultRouter()
router.register(r'vehiculos',views.VehiculoView,'vehiculos')
router.register(r'clientes',views.ClienteView,"clientes")
router.register(r'inspecciones',views.InspeccionView,"inspecciones")



urlpatterns = [
    
    path("v1/",include(router.urls))
]
