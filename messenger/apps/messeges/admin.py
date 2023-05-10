from django.contrib import admin

from messeges.models import BannedWord, Chat, Message


@admin.register(BannedWord)
class BannedWordAdmin(admin.ModelAdmin):
    """BannedWordAdmin."""

    model = BannedWord

    search_fields = ()
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted'
    )
    list_filter = (
        'datetime_created',
    )
    list_display = (
        'value',
        'datetime_created',
    )
    ordering = (
        '-datetime_created',
    )


admin.site.register(Chat)
admin.site.register(Message)
