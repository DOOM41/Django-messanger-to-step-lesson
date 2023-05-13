from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from abstractions.utils import check_user_name


User = get_user_model()


@receiver(pre_save, sender=User)
def my_handler(sender, instance, **kwargs):
    """Pre-save User."""
    if check_user_name(instance.first_name):
        raise Exception("Некорректное имя пользователя")

    if check_user_name(instance.last_name):
        raise Exception("Некорректная фамилия пользователя")

    instance.first_name = instance.first_name.title()
    instance.last_name = instance.last_name.title()
