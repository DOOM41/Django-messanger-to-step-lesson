# Django
from django.core.management.base import BaseCommand

# Python
import time
import random
import names
import threading

# Third-party
from auths.models import CustomUser


class Command(BaseCommand):
    """
    Generating users.
    """

    def __generate_password(self) -> str:
        symbols: str = 'abcdefghijklmnopqrstuvwxyz12345667890'
        password: str = ''
        for _ in range(30):
            password += random.choice(symbols)
        return password

    def __generate_email(self) -> str:
        domain: str = random.choice((
            'mail.ru', 'gmail.com', 'yahoo.ru', 'list.ru', 'inbox.ru'
        ))
        main: str = names.get_last_name()+names.get_first_name()
        email: str = main+str(random.randrange(1, 99999))+'@'+domain
        print(main, domain)
        return email

    def _generate_users(self, *args: tuple, **kwargs: dict) -> None:
        """
        Generating os users.
        """
        for _ in range(1200):
            password = self.__generate_password()
            email = self.__generate_email()
            u: CustomUser = CustomUser(
                password=password,
                email=email,
                username=email,
                last_name=names.get_last_name(),
                first_name=names.get_first_name()
            )
            u.set_password(password)
            u.save()

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """
        Handle method to start generating.
        """
        start = time.perf_counter()
        self._generate_users(*args, **kwargs)
        end = time.perf_counter()
        print(f' [i] Data was created in {end-start} seconds.')
