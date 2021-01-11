from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (IsAdminUser, )
from rest_framework.response import Response

from utils.permissions import (IsOwner, IsStaffUser)
from authentication.serializers import UserSerializer

from authentication.models import User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, pk=None):
        return Response('User has been deleted successfully')

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that the view requires
        """
        permission_classes = []
        if self.action == "list":
            permission_classes = [IsAdminUser, IsStaffUser]
            print('List action executed')
        elif self.action == 'retrive':
            permission_classes = [IsAdminUser, IsStaffUser, IsOwner]
            print('Retrieve action executed')
        elif self.action == 'delete':
            permission_classes = [IsAdminUser, IsOwner]
            print('Delete action executed')
        elif self.action == 'update':
            print('Update action executed')
            permission_classes = [IsAdminUser, IsOwner]
        elif self.action == 'partial_update':
            print('Partial update action executed')
            permission_classes = [IsAdminUser, IsOwner]
        else:
            pass
        return [permission() for permission in permission_classes]