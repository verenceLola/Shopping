from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NotificationsConsumer(AsyncJsonWebsocketConsumer):
    """
    notification consumer
    """

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("budget", self.channel_name)

    async def disconnect(self):
        await self.channel_layer.group_discard("budget", self.channel_name)

    async def budget(self, event):
        await self.send_json(event)
