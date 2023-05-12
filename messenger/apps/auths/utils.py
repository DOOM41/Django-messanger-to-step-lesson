from django.contrib.auth import get_user_model


class Get_user_model:
    def get_active_user_model():
        User = get_user_model()
        return User