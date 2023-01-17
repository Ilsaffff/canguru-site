from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models


class UserCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserDetailSerializer


class UsersListView(generics.ListAPIView):
    serializer_class = serializers.UserListSerializer
    queryset = models.User.objects.all()


class UserDetatilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserDetailSerializer
    queryset = models.User.objects.all()
