from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegistrSerializer(serializers.ModelSerializer):
    password_retry = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_retry']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password_retry = self.validated_data['password_retry']
        if password != password_retry:
            raise serializers.ValidationError({password: 'Пароль не совпадает'})
        user.set_password(password)
        user.save()
        return user
