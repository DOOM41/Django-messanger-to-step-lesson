# Django
from django.shortcuts import render
from django.db.models.query import QuerySet

# DRF
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework import status

# Local
from messeges.models import (
    Chat,
    Message
)
from messeges.serializers import MessageSerializers, ChatSerializer
from auths.models import CustomUser


class ChatMessageViewSet(ViewSet):
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
    
class CreateChatViewSet(ViewSet):
    def create(self, request):
        user_ids = request.data.get('unique_id') 
        is_it_many = request.data.get('is_many')

        users = CustomUser.objects.filter(id__in=user_ids)

        nicknames = [user.nickname for user in users]
        if len(set(nicknames)) != len(nicknames):
            prefix = '1' if is_it_many else '2'

            for user in users:
                user.nickname = f"{user.nickname}_{prefix}"
                user.save()

        chat = Chat.objects.create(is_many=is_it_many)

        chat.members.set(users)

        return Response({'chat_id': chat.id}, status=status.HTTP_201_CREATED)