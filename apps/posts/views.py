from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Post
from .serializers import PostSerializer


class PostView(ListCreateAPIView):
    """View for Post."""
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer