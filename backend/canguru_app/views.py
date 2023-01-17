from django.shortcuts import render
from rest_framework import generics
from . import serializers


class UserCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
