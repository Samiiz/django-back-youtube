from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routes import websoket_urlpatterns

applications = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})