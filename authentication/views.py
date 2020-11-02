from django.shortcuts import render
from authentication.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from authentication.models import User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer