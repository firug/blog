import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ArticleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.article_id = self.scope['url_route']['kwargs']['article_id']
        self.room_group_name = f'article_{self.article_id}'
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Отключаемся от группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправляем сообщение всем в группе
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'article_update',
                'message': message
            }
        )

    async def article_update(self, event):
        message = event['message']

        # Отправляем сообщение клиенту
        await self.send(text_data=json.dumps({
            'message': message
        }))
