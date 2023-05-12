# Django
from django.shortcuts import render
from django.db.models.query import QuerySet

# DRF
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

# Local
from messeges.models import (
    Chat,
    Message
)
from messeges.serializers import MessageSerializers, ChatSerializer


class ChatViewSet(ViewSet):
    """
    ViewSet Chats
    """

    queryset: QuerySet[Message] = Message.objects.select_related(
        'to_send'
    ).all()

    @action(
        methods=['GET'],
        detail=False
    )
    def list_chats(self, request: Request, *args: tuple) -> Response:
        chats = [message.to_send for message in self.queryset]
        serializer = ChatSerializer(
            chats, many=True
        )
        return Response(
            serializer.data,
            status=200
        )
