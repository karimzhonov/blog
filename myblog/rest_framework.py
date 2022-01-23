from rest_framework import serializers
from .models import *


class PostRest(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentsRest(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        