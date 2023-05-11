from django.contrib.auth import get_user_model

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from abstractions.utils import generate_code
from .tasks import send_code


User = get_user_model()


class VerifyView(APIView):
    """View for verificate user's email."""

    def post(
        self,
        request: Request
    ) -> Response:
        user_email = request.data.get('email')

        if not user_email:
            return Response({
                'error': 'Bad request'
            }, status=401)

        user: User = User.objects.filter(email=user_email).first()

        if not user:
            return Response({
                'error': 'User not found'
            }, status=401)

        user.verify_code = generate_code(User.VERIFY_CODE_SIZE)
        user.save()

        send_code.delay(email=user.email, verify_code=user.verify_code)

        return Response({
            'result': 'Verify code sended.'
        }, status=200)

    def get(
        self,
        request: Request
    ) -> Response:
        code: str = request.query_params.get('code')

        if not code:
            return Response({
                'error': 'Bad request'
            }, status=401)

        user: User = User.objects.filter(verify_code=code).first()

        if not user:
            return Response({
                'error': 'User not found'
            }, status=401)

        user.is_verifed = True
        user.save()

        return Response({
            'result': 'User is verified.'
        })
