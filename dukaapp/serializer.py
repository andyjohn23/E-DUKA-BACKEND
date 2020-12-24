from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:

        model = Profile
        fields = ('user', 'profile_picture', 'bio')


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSignupSerializer, self).create(validated_data)

class LogoutSerializer(serializers.Serializer):
    refresh_token=serializers.CharField()
    
    
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['merchant_name','description','date_started','category']