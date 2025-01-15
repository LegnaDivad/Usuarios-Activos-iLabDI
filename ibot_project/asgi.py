import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from laboratorio import consumers  # Import consumers from your laboratorio app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ibot_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles HTTP requests
    "websocket": AuthMiddlewareStack(  # Handles WebSocket connections
        URLRouter([
            path('ws/checadas/', consumers.ChecadasConsumer.as_asgi()),  # WebSocket route
        ])
    ),
})
