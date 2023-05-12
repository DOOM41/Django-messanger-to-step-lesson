from rest_framework import serializers

from messeges.models import Chat
from auths.models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class MessageSerializers(serializers.Serializer):
    """
    Serializer for get all message field
    """

    sender: CustomUser = UserSerializer()
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