from .models import IncorrectUserName


def check_user_name(name: str) -> bool:
    name = name.lower()

    if not name.isalpha():
        return True

    incorrect_names = [x.lower() for x in IncorrectUserName.objects.all()]

    if name in incorrect_names:
        return True
