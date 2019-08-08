from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]




class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    timestamp = serializers.DateTimeField(format="%d-%m-%Y %H:%I", read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
        ]

        read_only_fields = ['user']

    def validate_content(self, value):
            #Check that the post is not empty.
            if  not value:
                raise serializers.ValidationError("Post couldn't be empty")
            return value
