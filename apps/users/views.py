from django.shortcuts import render
from apps.users.models import User
from rest_framework import generics
from apps.users.serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    user = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]