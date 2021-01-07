from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth.password_validation import validate_password

from authentication.models import User

class UserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    confirm_password = CharField(write_only=True, required=True)

    def validate(self, attrs):
        if str(attrs['password']) != str(attrs['confirm_password']):
            raise ValidationError({'password': 'The passwords must match'})
        if not attrs['first_name']:
            raise ValidationError({'first_name': 'First name cannot be empty'})
        return attrs

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        user = super(UserSerializer, self).update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
            return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password','confirm_password', 'is_admin', 'is_active']