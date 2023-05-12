import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractUser, 
    PermissionsMixin,
    BaseUserManager
)
from django.core.exceptions import ValidationError

from decouple import config

class CustomUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        if not email:
            raise ValidationError('Email required')

        custom_user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        custom_user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.is_superuser = True
        custom_user.is_active = True
        custom_user.is_staff = True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return

    def create_test_user(self) -> 'CustomUser':

        custom_user: 'CustomUser' = self.model(
            email=self.normalize_email(config('EMAIL_TEST_USER', cast=str)),
            password=config('PASSWORD_TEST_USER', cast=str)
        )
        custom_user.set_password(config('PASSWORD_TEST_USER', cast=str))
        custom_user.save(using=self._db)
        return custom_user


class CustomUser(AbstractUser, PermissionsMixin):
    """
    Custom user model.
    """

    email = models.EmailField(
        verbose_name="почта/логин",
        unique=True
    )
    is_verifed = models.BooleanField(
        verbose_name='verifed',
        default=False
    )
    unique_id = models.UUIDField(
        verbose_name='уникальный идентификатор',
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    nickname = models.CharField(
        verbose_name='никнейм',
        max_length=255,
        unique=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"