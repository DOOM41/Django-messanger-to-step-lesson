from django.contrib import admin

from messeges.models import (
    Chat,
    Message
)


admin.site.register(Chat)
admin.site.register(Message)
