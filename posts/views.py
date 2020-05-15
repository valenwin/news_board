from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    @action(detail=True)
    def upvote(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        post.upvotes += 1
        post.save()
        return Response({'response': f'You like {post.id} post.'},
                        status=status.HTTP_200_OK)
