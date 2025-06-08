
from django.urls import include, path
from rest_framework import routers
from autocheckxapi import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'vehiculos',views.VehiculoView,'vehiculos')
router.register(r'clientes',views.ClienteView,"clientes")
router.register(r'inspecciones',views.InspeccionView,"inspecciones")



urlpatterns = [
    path('v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("v1/",include(router.urls))
]
