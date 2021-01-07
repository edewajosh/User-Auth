from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from utils.permissions import IsOwner
from authentication.serializers import UserSerializer

from authentication.models import User

class UserViewSet(ModelViewSet):
    permission_classes = [IsOwner|IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer