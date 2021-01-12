from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:

        model = Profile
        fields = ('id','user','username','avatar', 'address', 'phone_number','region')


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
        fields = ['id','category','image','card','shop']
        
class Sub_CategorySerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.category')
    class Meta:
        model = Sub_Category
        fields = ['id','name','description','category']
        
class ProductSerializer(serializers.ModelSerializer):
    # sub_category = serializers.CharField(source='sub_category.name')
    class Meta:
        model = Product
        fields = ['id','item_name','description','price','date_added','sub_category','quantity','color','previous_price','size','brand','image','image1','image2','image3']
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','user','comment','product_id']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user','date','product_id']