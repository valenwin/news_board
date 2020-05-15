from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField(read_only=True)
    updated = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    def get_created(self, instance):
        return instance.created.strftime("%B %d, %Y, %H:%M")

    def get_updated(self, instance):
        return instance.updated.strftime("%B %d, %Y")


class CommentSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField(read_only=True)
    updated = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        comment = Comment(**validated_data)
        comment.save()
        return comment

    def get_created(self, instance):
        return instance.created.strftime("%B %d, %Y, %H:%M")

    def get_updated(self, instance):
        return instance.updated.strftime("%B %d, %Y")
