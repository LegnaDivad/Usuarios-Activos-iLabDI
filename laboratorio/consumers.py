import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
from asgiref.sync import sync_to_async

class ChecadasConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "checadas_room"
        self.room_group_name = "checadas"

        # Unirse al grupo
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Enviar checadas iniciales al conectar
        await self.enviar_checadas()

    async def disconnect(self, close_code):
        # Salir del grupo
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')

        if message == 'actualizar':
            # Si el mensaje es 'actualizar', enviamos las checadas nuevamente
            await self.enviar_checadas()

    async def enviar_checadas(self):
        """Consulta las checadas y las envía al cliente."""
        checadas = await self.get_checadas()

        # Enviar las checadas al grupo
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_checadas',
                'checadas': checadas
            }
        )

    @sync_to_async
    def get_checadas(self):
        """Realiza la consulta a la base de datos de manera sincrónica."""
        from laboratorio.models import Checadas

        checadas_qs = Checadas.objects.select_related('identificador').all()

        # Convertimos el QuerySet a una lista de diccionarios
        checadas = [
            {
                "nombre": checada.identificador.nombre,
                "codigo": checada.identificador.codigo,
                "fechaEntrada": checada.fechaEntrada.strftime('%Y-%m-%d') if checada.fechaEntrada else '',
                "horaEntrada": checada.horaEntrada.strftime('%H:%M:%S') if checada.horaEntrada else '',
                "fechaSalida": checada.fechaSalida.strftime('%Y-%m-%d') if checada.fechaSalida else '',
                "horaSalida": checada.horaSalida.strftime('%H:%M:%S') if checada.horaSalida else '',
                "horas": checada.horas.strftime('%H:%M:%S') if checada.horas else ''
            }
            for checada in checadas_qs
        ]
        return checadas

    async def send_checadas(self, event):
        checadas = event['checadas']

        # Enviar las checadas al WebSocket
        await self.send(text_data=json.dumps({
            'checadas': checadas
        }))
