from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class BaseTemplateView(TemplateView):
    template_name = "base.html"


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    @action(detail=True)
    def upvote(self, request, pk):
        """
        Upvote the post by using post id
        """
        post = get_object_or_404(Post, id=pk)
        post.upvotes += 1
        post.save()
        return Response(
            {"response": f"You upvoted {post.id} post."}, status=status.HTTP_200_OK
        )

    @action(detail=True)
    def comments(self, request, pk):
        """
        Get comments for each post by using post id
        """
        comments = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    @action(detail=True)
    def post(self, request, pk):
        """
        Get post information for each comment by using comment id
        """
        comment = get_object_or_404(Comment, id=pk)
        post = get_object_or_404(Post, id=comment.post.id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
