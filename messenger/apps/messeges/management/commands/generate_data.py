# Python
import uuid
import random
from typing import Any
from datetime import timedelta
from random import randint

# Django
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

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
            username = str(uuid.uuid4())[:8]
            email = f'{username}@example.com'
            password = 'password'
            user = User.objects.create_user(
                email=email, password=password)
            print(f'Created user with ID: {user.id}')

    def generate_chats_and_messages(self):
        User = get_user_model()
        random_object = User.objects.order_by('?').first()
        # Generate Chats
        for i in range(5):
            chat = Chat.objects.create(
                owner=random_object, name=f"Chat{i}", is_many=random.choice([True, False]))
            # Generate Messages for each Chat
            for _ in range(10):
                sender = random_object
                text = f'Message from {sender.email}'
                datetime_send = timezone.now() - timedelta(days=randint(0, 7))
                message = Message.objects.create(
                    sender=sender, to_send=chat, text=text, datetime_send=datetime_send)

            print(f'Created Chat and Messages with ID: {chat.id}')

    def handle(self, *args: Any, **kwargs: Any) -> None:
        self.generate_users()
        self.generate_chats_and_messages()
