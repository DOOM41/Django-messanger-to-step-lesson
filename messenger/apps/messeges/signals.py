# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Local
from .models import Message
from .utils import write_messages_to_excel


@receiver(post_save, sender=Message)
def export_message(sender, instance, **kwargs):
    messages = Message.objects.filter(id=instance.id)
    print(messages)
    write_messages_to_excel(messages)
    print('Понятно, так и запишем...')
    