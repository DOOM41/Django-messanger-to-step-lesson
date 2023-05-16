from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from phonenumbers import parse, is_valid_number


class CustomUser(AbstractUser, PermissionsMixin):
    """
    Custom user model.
    """
    
    phone_regex: RegexValidator =\
        RegexValidator(
            regex=r'^+?1?\d{9,15}$', 
            message="Номер телефона должен быть введен в формате: '+999999999'. Допустимая длина от 9 до 15 цифр."
        )
    
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    email = models.EmailField(
        verbose_name="почта/логин",
        unique=True
    )

    def save(self, args, kwargs):
        try:
            parsed_number = parse(self.phone_number, None)
            if not is_valid_number(parsed_number):
                raise ValueError('Некорректный номер телефона')
        except:
            raise ValueError('Некорректный номер телефона')
        super(CustomUser, self).save(args, kwargs)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"