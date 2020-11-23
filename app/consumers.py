import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer
from channels.layers import get_channel_layer

users = {}


class ReactConsumer(JsonWebsocketConsumer):
    def connect(self):
        if self.channel_name not in users:
            users[self.channel_name] = self.channel_name
        self.accept()
        self.send_json({'type': 'yourID', 'yourid': self.channel_name})
        self.send_json({'type': 'allUsers', 'allusers': users})

    def disconnect(self, code):
        if self.channel_name in users:
            del users[self.channel_name]

    def call_user(self, message):
        message = json.loads(message['text'])
        self.send_json({'type': 'hey', 'from': message['payload']['from'], 'signal': message['payload']['signal']})

    def accept_call(self, message):
        message = json.loads(message['text'])
        self.send_json({'type': 'callAccepted', 'signal': message['payload']['signal']})

    def receive_json(self, payload, **kwargs):
        if payload[0] == "callUser":
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.send)(payload[1]['userToCall'], {
                "type": "call_user",
                "text": json.dumps({
                    'type': 'hey',
                    'payload': {
                        'signal': payload[1]['signalData'],
                        'from': payload[1]['from']
                    }
                }),
            })

        if payload[0] == "acceptCall":
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.send)(payload[1]['to'], {
                "type": "accept_call",
                "text": json.dumps({
                    'type': 'callAccepted',
                    'payload': {
                        'signal': payload[1]['signal'],
                    }
                }),
            })
        print('websocket_receive')


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('connect')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
