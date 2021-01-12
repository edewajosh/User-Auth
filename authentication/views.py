from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (IsAdminUser, )
from rest_framework.response import Response
from rest_framework import status

from utils.permissions import (IsOwner, IsStaffUser)
from authentication.serializers import UserSerializer

from authentication.models import User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, pk=None):
        return Response('User has been deleted successfully')

    def partial_update(self, request, *args, **kwargs):
        serialized = UserSerializer(request.user, data=request.data, partial=True)
        #return self.update(request, *args, **kwargs)
        return Response(status=status.HTTP_202_ACCEPTED)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that the view requires
        """
        permission_classes = []
        if self.action == "list":
            permission_classes = [IsAdminUser | IsStaffUser]
        elif self.action == 'retrive':
            permission_classes = [IsAdminUser | IsStaffUser | IsOwner]
        elif self.action == 'delete':
            permission_classes = [IsAdminUser | IsOwner]
        elif self.action == 'update':
            permission_classes = [IsAdminUser | IsOwner]
        elif self.action == 'partial_update':
            permission_classes = [IsAdminUser|IsOwner]
        else:
            pass
        return [permission() for permission in permission_classes]