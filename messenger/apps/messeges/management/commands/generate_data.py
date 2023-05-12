# Python
from typing import Any
from datetime import datetime, timedelta
from requests.models import Response

# Django
from django.core.management.base import BaseCommand
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import get_user_model
from django.utils import timezone
from random import randint, choice

# Local
from messeges.models import (
    Chat,
    Message
)


class Command(BaseCommand):
    """Custom command for filling up database."""

    help = 'Custom command for filling up database'

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    def generate_users(self) -> None:
        User = get_user_model()
        for i in range(10):
            email = f'user_{i}@gmail.com'
            user = User.objects.create_user(
                email=email, password='password')

            print(f'Created user number: {i} ')

    def generate_chats_and_messages(self):
        User = get_user_model()
        random_object = User.objects.order_by('?').first()
        # Generate Chats
        for _ in range(5):
            chat = Chat.objects.create(owner=random_object, name=f"Chat{_}")
            # Generate Messages for each Chat
            for _ in range(10):
                sender = random_object
                text = f'Message from {sender.email}'
                datetime_send = timezone.now() - timedelta(days=randint(0, 7))
                message = Message.objects.create(
                    sender=sender, to_send=chat, text=text, datetime_send=datetime_send)

            print(f'Created Chat with ID: {chat.id} and Messages')

    def handle(self, *args: Any, **kwargs: Any) -> None:
        self.generate_users()
        self.generate_chats_and_messages()
