from rest_framework import generics
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class ListCreateGroup(generics.ListCreateAPIView):
    queryset = Group.objects.all().order_by("-id")
    serializer_class = GroupSerializer




class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser

        exclude = ("last_login", "is_superuser", "is_staff", "date_joined", "user_permissions", "is_active")

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise Exception("Passwords do not match.")
        
        return data

    def create(self, validated_data):
        del validated_data["password2"]
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class ListCreateUser(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by("-id")
    serializer_class = CustomUserSerializer
