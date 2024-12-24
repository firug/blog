from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/article/<int:article_id>/', consumers.ArticleConsumer.as_asgi()),
]