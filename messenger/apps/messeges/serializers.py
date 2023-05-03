from rest_framework import serializers
from django.contrib.auth.models import User

from messeges.models import Chat


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User."""
    
    class Meta:
        model = User
        fields = '__all__'


class MessageSerializers(serializers.Serializer):
    """
    Serializer for get all message field.
    """

    sender: User = UserSerializer()
    to_send: Chat = serializers.PrimaryKeyRelatedField(
        queryset = Chat.objects.all()
    )
    text = serializers.CharField()
    datetime = serializers.DateTimeField()

    class Meta():
        fields = (
            'sender',
            'to_send',
            'text',
            'datetime',
        )


class ChatSerializer(serializers.Serializer):
    """Serializer for Chat."""

    owner = UserSerializer(required=False)
    is_many = serializers.BooleanField(read_only=True)
    name = serializers.CharField()
    members = UserSerializer(many=True)

    class Meta:
        fields = (
            'owner',
            'is_many',
            'name',
            'members',
        )
