from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:

        model = Profile
        fields = ('user', 'profile_picture', 'bio')


