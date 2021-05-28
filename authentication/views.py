from django.shortcuts import render
from django.core.mail import send_mail

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        send_mail(
            'Subject here',
            'Here is the message.',
            ['joshedewa@gmail.com'],
            fail_silently=False,
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, pk=None):
        return Response('User has been deleted successfully')

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # if 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that the view requires
        """
        permission_classes = []
        if self.action == "list":
            permission_classes = [IsAdminUser | IsStaffUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAdminUser | IsStaffUser | IsOwner]
        elif self.action == 'delete':
            permission_classes = [IsAdminUser | IsOwner]
        elif self.action == 'update':
            permission_classes = [IsAdminUser | IsOwner]
        elif self.action == 'partial_update':
            permission_classes = [IsAdminUser | IsOwner]
        elif self.action == 'create':
            permission_classes = [IsAdminUser | IsStaffUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
