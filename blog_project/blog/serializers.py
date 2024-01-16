from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'publish_date']

class CommentSerializer(serializers.ModelSerializer):
    modal = Comment
    fields = ['id', 'title', 'content', 'author', 'publish_date']
    