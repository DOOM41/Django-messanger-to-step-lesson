from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
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


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.
    """

    email = models.EmailField(
        verbose_name="почта/логин",
        unique=True
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=150
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=150
    )
    is_active = models.BooleanField(
        verbose_name='активный пользователь',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='штатный сотрудник',
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name='администратор',
        default=False
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


class IncorrectUserName(models.Model):
    """IncorrectUserName.

    Модель для хранения некорректных имен пользователя
    """

    value: str = models.CharField(
        max_length=100,
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'Incorrect user name'
        verbose_name_plural = 'Incorrect user names'

    def __str__(self) -> str:
        return self.value
