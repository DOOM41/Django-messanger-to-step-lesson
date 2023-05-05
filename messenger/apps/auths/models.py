from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser, PermissionsMixin):
    """
    Custom user model.
    """

    email = models.EmailField(
        verbose_name="почта/логин", unique=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
