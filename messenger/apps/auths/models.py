# Django
from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.exceptions import ValidationError



class CustomUserManager(BaseUserManager):
    """
    User Manager.
    """

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
            email=self.normalize_email('root2@gmail.com'),
            password='qwerty'
        )
        custom_user.set_password('qwerty')
        custom_user.save(using=self._db)
        return custom_user


class CustomUser(
    AbstractUser,
    PermissionsMixin
):
    """
    Custom User.
    """
    

    email = models.EmailField(
        verbose_name='email',
        unique=True
    )
    password = models.CharField(
        verbose_name='password',
        max_length=100
    )
    first_name = models.CharField(
        verbose_name='firstname',
        max_length=60,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='lastname',
        max_length=70,
        null=True,
        blank=True
    )
    is_superuser = models.BooleanField(
        verbose_name='superuser',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='active',
        default=False
    )
    is_verified = models.BooleanField(
        verbose_name='verifed',
        default=False
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args, **kwargs) -> None:
        return super().save(*args , **kwargs)