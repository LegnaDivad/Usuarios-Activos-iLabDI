# laboratorio/urls.py

from django.urls import path
from .views import checadas_view  # Importamos la vista
from  laboratorio import consumers

urlpatterns = [
    path('templates/', checadas_view, name='usuarios_activos_inactivos'),  # Ruta para la vista
]

websocket_urlpatterns = [
    path('ws/checadas/', consumers.ChecadasConsumer.as_asgi()),
]
