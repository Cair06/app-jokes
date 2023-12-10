from random import choice

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task


channel_layer = get_channel_layer()


@shared_task
def get_joke():
    with open('/home/rasalghoul/Downloads/projects/python/app-jokes/jokes_proj/jokes/jokes.txt', 'r') as file:
        lines = file.readlines()
    joke = choice(lines)

    async_to_sync(channel_layer.group_send)('jokes', {'type': 'send_jokes', 'text': joke})