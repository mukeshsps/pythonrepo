from rest_framework import serializers
from .models import Mall
from .models import Shop
from django.contrib.auth.models import User
from .models import Product
from .models import Order, UserProfile
from django.contrib.auth.password_validation import validate_password
from .models import WishList
from rest_framework.validators import UniqueValidator
from api.models import Cart


class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = ('id', 'MName', 'MCategory', 'MAddress', 'M_image', 'M_Status')#, 'date_created', 'date_modified')
        #read_only_fields = ('date_created', 'date_modified')
        
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'SName', 'SCategory', 'Shop_number', 'Shop_type', 'S_status', 'Product_type', 'Shop_location')#, 'date_created', 'date_modified')
        #read_only_fields = ('date_created', 'date_modified')
    
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
             
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'P_name', 'P_image', 'p_Cost', 'P_status', 'P_features')#, 'date_created', 'date_modified')
        #read_only_fields = ('date_created', 'date_modified')
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'customer_address', 'Phone_number', 'Order_date')
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile 
        error_messages = {"full_name": {"required": "Give yourself a full_name"}}
        fields = ('full_name', 'address', 'phone_number')
     
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    class Meta:
        fields =('id', 'old_password', 'new_password')
    def validate_new_password(self, value):
        validate_password(value)
        return value  
    
class UserSerializer(serializers.ModelSerializer):
    user= UserProfileSerializer()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User   
        fields = ( 'id', 'username', 'user', 'email', 'password')
        
    def create(self, validated_data):
        profile_data = validated_data.pop('user')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user
                            
class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        field = ('id', 'product_id', 'date_created', 'date_modified')
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        field = ('id', 'product_id', 'date_created', 'date_modified')
