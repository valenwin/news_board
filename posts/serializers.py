from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('update',)

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post
