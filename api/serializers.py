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
        
"""class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='UserProfile.full_name')
    address = serializers.CharField(source='UserProfile.full_name')
    phone_number = serializers.CharField(source='UserProfile.full_name')        
        
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'full_name', 'address', 'phone_number')
        #read_only_fields = ('date_created', 'date_modified') 
    #def create(self, validated_data, attrs, instance=None):
    def create(self, attrs, instance=None):
        if instance is not None:
            instance.full_name = attrs.get('fullname', instance.full_name)
            instance.address = attrs.get('address', instance.address)
            instance.phone_number = attrs.get('phone_number', instance.phone_number)
            return instance
        user = User.objects.create_user(username=attrs.get('user.username'), email= attrs.get('user.email'), password=attrs.get('user.password'))
        user.save()
        #return serializers.ModelSerializer.create(self, validated_data, user=user)
        return User(user)"""
    
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
    
    """def create(self, validated_data):
        profile_data = validated_data.pop('user')
        user = UserProfile.objects.create(**validated_data)
        User.objects.create(user=user, **profile_data)
        return user"""
    
"""
def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        representation['UserProfile'] = UserProfileSerializer(instance.UserProfile_set.all(), many=True).data
        return representation"""  
        
"""class UserProfileSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password')
    #full_name = serializers.CharField(source='UserProfile.full_name') 
    #address = serializers.CharField(source='UserProfile.address')
    #phone_number = serializers.CharField(source='UserProfile.phone_number')
    class Meta:
        model = UserProfile 
        fields = ('username','full_name', 'address', 'phone_number', 'email', 'password')
        
    def create(self, attrs, instance=None):
        if instance is not None:
            #instance.id = attrs.get('id', instance.id)
            instance.username = attrs.get('username', instance.username)
            instance.email = attrs.get('email', instance.email)
            instance.password = attrs.get('password', instance.password)
            return instance.string.strip()
        print("instance")
        #user = User.objects.create_user(username=attrs.get('user.username'), email= attrs.get('user.email'), password=attrs.get('user.password'))
        user = User.objects.create_user(username=User.username,password=User.password,email=User.email)
        return UserProfile(user)"""    
    
    
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