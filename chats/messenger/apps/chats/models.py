from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

User: AbstractBaseUser = get_user_model()


class ChatManager(models.Manager):
    """
    Manager for Chat model.
    """
    def get_all_chats(self):
        return self.all()

    def get_chat_by_id(self, chat_id):
        try:
            return self.get(id=chat_id)
        except Chat.DoesNotExist:
            return None
    
    def get_chat_by_owner_id(self, owner_id, chat_id):
        try:
            return self.get(owner_id=owner_id, id=chat_id)
        except Chat.DoesNotExist:
            return None
    
    def get_chats_by_owner(self, owner_id):
        return self.filter(owner_id=owner_id)


class Chat(models.Model):
    """
    Chat can be 1 people or group chat 
    """
    owner: 'User' = models.ForeignKey(
        to=User,
        related_name="own_chats",
        on_delete=models.CASCADE,
        verbose_name="Создатель",
        null=True,
        blank=True
    )
    is_many: bool = models.BooleanField(
        verbose_name="Groop?",
        default=False
    )
    name: str = models.CharField(
        verbose_name="Name",
        max_length=120
    )
    members: list['User'] = models.ManyToManyField(
        to=User,
        related_name="chats"
    )

    objects = ChatManager()
    
    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = "Chat"
        verbose_name_plural = "Chats"

    def __str__(self) -> str:
        return (
            f"Owner : {self.owner if self.owner is not None else 'Basic'}"
            f"Count users: {len(self.members.get_queryset())}"
        )


class Message(models.Model):
    """
    Messege between users.
    """
    sender: "User" = models.ForeignKey(
        to=User,
        related_name='messeges',
        verbose_name='сообщения',
        on_delete=models.CASCADE
    )
    to_send: "Chat" = models.ForeignKey(
        to=Chat,
        related_name="messeges",
        verbose_name="chat",
        on_delete=models.CASCADE
    )
    text: str = models.TextField(
        verbose_name="messege",
        max_length=2000
    )
    datetime_send = models.DateTimeField(
        verbose_name='Время отправления',
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        ordering = (
            '-datetime_send',
        )
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self) -> str:
        return f"[{self.datetime_send.strftime('%d %B - %H:%M:%S')}] {self.sender} : {self.text}"
