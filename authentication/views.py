from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (IsAdminUser, )
from rest_framework.response import Response
from rest_framework import status

from authentication.token import account_activation_token
from utils.permissions import (IsOwner, IsStaffUser)
from authentication.serializers import UserSerializer

from authentication.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        current_site = get_current_site(request)
        email_subject = 'Activate Your Account'
        # Call save method to the user id
        message = render_to_string(
            'email/activate_account.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user)
            }
        )
        to_email = user.email
        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, pk=None):
        return Response('User has been deleted successfully')

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # if 'prefetch_related' has been applied to a queryset, we need to
            # refresh the instance from the database
            instance = self.get_object()
            serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user = serializer.save()
        return user

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that the view requires
        """
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
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


def activate_account(request, uuid64, token):
    try:
        uuid = force_bytes(urlsafe_base64_encode(uuid64))
        user = User.objects.get(uuid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response('Your account has been activate successfully')
    else:
        return Response('Activation link is invalid!')
