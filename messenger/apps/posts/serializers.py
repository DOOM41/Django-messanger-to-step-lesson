from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for post."""

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "description",
            "image"
        )