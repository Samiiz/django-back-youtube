from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routes import websoket_urlpatterns
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            websoket_urlpatterns
        )
    )
})