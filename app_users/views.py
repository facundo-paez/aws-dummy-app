from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []
    queryset = User.objects.all()
