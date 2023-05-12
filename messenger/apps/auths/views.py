# Django
from django.shortcuts import render
from django.db.models.query import QuerySet

# DRF
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

# Local
from .models import CustomUser
from messeges.serializers import UserSerializer


class UserViewSet(ViewSet):
    """
    ViewSet Users
    """

    queryset: QuerySet[CustomUser] = CustomUser.objects.all()

    @action(
        methods=['GET'],
        permission_classes = [IsAdminUser],
        detail=False
    )
    def list_users(self, request: Request, *args: tuple) -> Response:
        serializer = UserSerializer(
            self.queryset, many=True
        )
        return Response(
            serializer.data,
            status=200
        )

   
