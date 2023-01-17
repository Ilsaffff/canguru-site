from rest_framework import serializers
from .models import *
from django import forms


class UserSerializer(serializers.ModelSerializer):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'