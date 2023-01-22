from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from . import serializers
from . import models
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import permissions

# from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = [permissions.AuthorAllStaffAllButEditOrReadOnly]


class RegistrUserView(CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRegistrSerializer
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)
