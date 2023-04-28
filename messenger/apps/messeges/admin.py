from django.contrib import admin

from messeges.models import (
    Chat,
    Message
)

admin.register(Chat)
admin.register(Message)
