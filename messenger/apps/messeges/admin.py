# Django
from django.contrib import admin

# Local
from messeges.models import (
    Chat,
    Message
)


admin.register(Chat)
admin.register(Message)
