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


class ChatMessageViewSet(ViewSet):
    """
    ViewSet Chats.
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

    @action(
        methods=['GET', 'POST'],
        detail=False
    )
    def list_messages(self, request: Request, *args: tuple) -> Response:
        if request.method == "GET":
            serializer = MessageSerializers(
                self.queryset, many=True
            )
            return Response(
                serializer.data,
                status=200
            )
        serializer: MessageSerializers = MessageSerializers(
            data=request.POST
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                'message': f"Message {serializer.validated_data.get('id')} is created"
            }
        )
    
