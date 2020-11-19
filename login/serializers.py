# from rest_framework import serializers
# from .models import MyUser, Post
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
#
# class GetAllSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = MyUser
#         fields = ('username','sodu',)
#
#
# class APISerializer(serializers.ModelSerializer):
#     username_post = serializers.CharField(max_length=12)
#     sodu_post = serializers.IntegerField(default=21)
#
#     class Meta:
#         # phải là model
#         model = Post
#         fields = ('username_post','sodu_post')

from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'sodu',)

