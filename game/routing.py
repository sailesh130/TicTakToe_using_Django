from django.conf.urls import url

from game.consumers import MygameConsumer

websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_code>\w+)/$', MygameConsumer.as_asgi()),
]