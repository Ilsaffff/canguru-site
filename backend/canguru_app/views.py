from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
