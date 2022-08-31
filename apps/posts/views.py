from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer,PostCreateSerializer,PostUpdateSerializer,PostDeleteSerializer
from .models import Post
# Create your views here.
class PostViewAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostUPdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer