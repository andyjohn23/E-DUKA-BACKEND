from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer(required=True)
#     class Meta:
#         model = User
#         fields = '__all__'

#     def create(self, validated_data):

#         # create user 
#         user = User.objects.create(
#             email = validated_data['email'],
#             first_name = validated_data['first_name'],
#             last_name = validated_data['last_name'],
#             date_joined = validated_data['date_joined'],
#             user_type = validated_data['user_type'],
#         )

#         profile_data = validated_data.pop('profile')
#         # create profile
#         profile = Profile.objects.create(
#             user = user,
#             username = profile_data['username'],
#             avatar = profile_data['avatar'],
#             address = profile_data['address'],
#             phone_number = profile_data['phone_number'],
#             region = profile_data['region'],
#         )

#         return user

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = Profile
        fields = ('id','username','user','avatar', 'address', 'phone_number','region')


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','user_type','email','first_name','last_name','password']
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
        model = Shop
        fields = ['id','store_name','description','date_started','address','city','country','phone_no']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category','image','card']
        
class Sub_CategorySerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.category')
    class Meta:
        model = Sub_Category
        fields = ['id','name','description','category','image2']
        
class ProductSerializer(serializers.ModelSerializer):
    # shipped_from = serializers.CharField(source='shipped_from.store_name')
    class Meta:
        model = Product
        fields = ['id','item_name','description','price','date_added','sub_category','quantity','color','previous_price','shipped_from','size','brand','image','image2','image3','image4']
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','user','comment','product_id']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'