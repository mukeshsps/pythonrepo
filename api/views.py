from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status, viewsets, filters
from .models import Mall
from .serializers import MallSerializer
from .models import Shop
from .serializers import ShopSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import Product
from .serializers import ProductSerializer
from django.http.response import HttpResponse, Http404
import datetime
from .form import LoginForm, PasswordResetRequestForm
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import Order
from .serializers import OrderSerializer
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.template.context_processors import request
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,\
    BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer, WishListSerializer
from django.views.generic.edit import FormView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template import loader
from django.core.mail import send_mail
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib import messages
from api.form import SetPasswordForm
from django.contrib.auth import get_user_model, login, hashers
from rest_framework.renderers import TemplateHTMLRenderer
from api.models import WishList
from rest_framework.decorators import api_view, permission_classes
from django.utils import translation
from django.utils.translation import gettext as _
from rest_framework.compat import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_401_UNAUTHORIZED,\
    HTTP_203_NON_AUTHORITATIVE_INFORMATION
import email
#import base64
#from django.contrib.auth.forms import UsernameField
#from MySQLdb.constants.ER import USERNAME
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework.backends import DjangoFilterBackend
# Create your views here.

class LocaleMiddleware(object):
    def process_request(self, request):
        language = translation.get_language_from_request(request)
        translation.activate(language)
        request.ar = translation.get_language()
        
    def process_response(self, request, response):
        translation.deactivate()
        return response



        
class createMallView(generics.ListCreateAPIView):
    queryset = Mall.objects.all()
    serializer_class = MallSerializer
    
    def perform_create(self, serializer):
        serializer.save()
    def get(self, request, *args, **kwargs):
        setattr(request, 'ar', 'en')
        return super().get(self, request, *args, **kwargs)
    
def model_form_upload(request):
        if request.method == 'POST':
            form = Mall(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = Mall()
        return render(request, '/model_form_upload.html', {
            'form': form
        })
      
class detailsMallView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mall.objects.all();
    serializer_class = MallSerializer
    
class createShopView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    
    def perform_create(self, serializer):
        serializer.save()

class detailsShopView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all();
    serializer_class = ShopSerializer
    
class fetchDataview(generics.RetrieveAPIView):
    queryset = Shop.objects.raw(' select shop.name, shoptype.id from shop LEFT JOIN shoptype on shop.id=shoptype.id order by shop.shop.name')
    serializer_class = ShopSerializer
    
class viewUserTable(generics.ListCreateAPIView):
    queryset = User.objects.raw('select * from auth_user')
    serializer_class = UserSerializer
    
class createProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        serializer.save()
# class for product details based on product list
"""class detailsProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer"""
  
class detailsProductView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def details(self, request):
        queryset = Product.objects.all()
        queryset = self.get_queryset(id)
        serializer = ProductSerializer(queryset, many=False)
        pdata = {'status':200,'response':serializer.data,'msg':"product successfully displayed"}
        return Response(pdata)

#the given view is used for mall list api view    
class MallsList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Mall.objects.all()
    serializer_class = MallSerializer
    permission_classes = (IsAdminUser,)
    model = Mall
    paginate_by = 10
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = MallSerializer(queryset, many=True)
        mdata = {'status':200,'response':serializer.data,'msg':"Mall List"}
        return Response(mdata)  
    
     
#the given view is used for shop list api view      
class Shoplist(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAdminUser,)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ShopSerializer(queryset, many=True)
        sdata = {'status':200,'response':serializer.data,'msg':"Shop List"}
        return Response(sdata)  

#the given view is used for Product list api view 
class Productlist(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer
    permission_class = (IsAdminUser,)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        mdata = {'status':200,'response':serializer.data,'msg':"Product List"}
        return Response(mdata)  


class SearchProductlist(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    model = Product
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'P_name')#, 'id')
    
    #def get_queryset(self):
    #   user = self.request.user
    #   return Product.objects.filter(P_name=user)
    
class SearchMall(generics.ListAPIView):
    permission_classes(IsAuthenticated,)
    model = Mall
    queryset = Mall.objects.all()
    serializer_class = MallSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'MName')
    
class SearchShop(generics.ListAPIView):
    permission_classes(IsAuthenticated,)
    model = Shop
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'SName')
    
class OrderCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class  = OrderSerializer
    
    def perform_create(self, serializer):
        serializer.save()
        
##the given view is used for creating order       
@api_view(['POST'])
@permission_classes((AllowAny,))       
def CreateOrder(request):
    serialized = OrderSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        codata = {'status':200, 'msg':("Product is Successfully Ordered")}
        return Response(codata)
    else:
        co1data = {'status':501, 'msg':"Something happning wrong"}
        return Response(co1data)



class OrderDeatilsView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class  = OrderSerializer
    
class OrderHistory(generics.ListAPIView):
    queryset = Order.objects.raw('select * from api_historicalorder')
    serializer_class  = OrderSerializer
    



class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class  = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response(status=200)
    
##the given view is used for create user 
@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request,):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():  
        instance = serialized.save()
        instance.set_password(instance.password)
        instance.save()
        sData = {'status':200,'response':serialized.data, 'msg':("User Successfully Registered")}
        return Response(sData)
    else:         
        s1data = {'status':501, 'msg':("Email or Username already exist")}
        return Response(s1data)
    
    

##the given view is used for user login        
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_user(request):
    authentication_classes = (SessionAuthentication)#(TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    language = 'ar'
    translation.activate(language)
    username = request.data.get("username")
    password = request.data.get("password")
    encoded = make_password(password)
    check_password(password, encoded)
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        login(request, user) 
        user= User.objects.get(pk=user.id)
        query = 'select full_name, address, phone_number from api_userprofile where user_id=user.id'
        user1 = UserProfile.objects.get(pk = request.user.pk)
        print(user1)
        print(user1.phone_number)           
        rs = {'id': user.id,'username':user.username,'email': user.email,'full_name':user1.full_name, 'address':user1.address, 'phone_number':user1.phone_number}
        ldata = {'status':200, 'response':rs,'msg':"User Successfully Logged"}
        return Response(ldata)
    else:
        if user is not None:
            if user.is_active:
                login(request, user)
                rs = {'id': user.id,'username':user.username,'email': user.email, 'full_name': user.userprofile.full_name}
                ldata = {'status':200,'response':rs,'msg':"User Successfully Login"}
                return Response(ldata) 
            else:
                u1data= {'status':501, 'msg':"User account is not valid"}
                return Response(u1data)
        else:
            u1data= {'status':501, 'msg':"Invalid Username or Password"}
            return Response(u1data)    
    l1data = {'status':501,' msg':"Invalid Username or Password"}
    return Response(l1data)
        

##the given view is used for update user password
#@login_required
class UpdatePassword(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object)
        serializer = ChangePasswordSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            id = serializer.data.get("id")
            print(id)
            old_password = serializer.data.get("old_password")
            print(old_password)
            encoded = make_password(old_password)
            print(encoded)
            check_password(old_password, encoded)
            if not self.object.check_password(old_password):
                pdata = {'status':500, 'msg':"Old password is: wrong password"}
                return Response(pdata)
                #return Response({"old_password": ["Wrong password."]}, 
                                #status=status.HTTP_400_BAD_REQUEST)
            new_password = serializer.data.get("new_password")
            print(new_password)
            self.object.set_password(new_password)
            #self.object.set_password(serializer.data.get("new_password"))
            print(self.object.set_password(serializer.data.get("new_password")))
            self.object.save()
            cdata = {'status':200,'msg':"New Password saved sucessfully"}
            return Response(cdata)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

                           
    
        
class WishListCreate(generics.ListCreateAPIView):
    queryset = WishList.objects.all()
    serializer_class  = WishListSerializer
    
    def perform_create(self, serializer):
        serializer.save()

class RemoveFromWishList(generics.DestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class  = WishListSerializer
    
   
    
class ResetPasswordRequestView(FormView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "registration/password_reset_email.html"
    success_url = '/api/login'
    form_class = PasswordResetRequestForm
    
    @staticmethod
    def validate_email_address(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data= form.cleaned_data["email_or_username"]
        if self.validate_email_address(data) is True: 
            associated_users= User.objects.filter(Q(email=data)|Q(username=data))
            if associated_users.exists():
                for user in associated_users:
                    c = {
                         'email': user.email,
                         'domain': request.META['HTTP_HOST'],
                         'site_name': 'your site',
                         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                         'user': user,
                         'token': default_token_generator.make_token(user),
                         'protocol': 'http',
                         }
                    subject_template_name='registration/password_reset_subject.txt' 
                            # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
                    email_template_name='registration/password_reset_email.html'    
                            # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
                    subject = loader.render_to_string(subject_template_name, c)
                            # Email subject *must not* contain newlines
                    subject = ''.join(subject.splitlines())
                    email = loader.render_to_string(email_template_name, c)
                    send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
                return result
            else:
                associated_users= User.objects.filter(username=data)
                if associated_users.exists():
                    for user in associated_users:
                        c = {
                            'email': user.email,
                            'domain': 'example.com', #or your domain
                            'site_name': 'example',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'user': user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                            }
                        subject_template_name='registration/password_reset_subject.txt'
                        email_template_name='registration/password_reset_email.html'
                        subject = loader.render_to_string(subject_template_name, c)
                        # Email subject *must not* contain newlines
                        subject = ''.join(subject.splitlines())
                        email = loader.render_to_string(email_template_name, c)
                        send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                    result = self.form_valid(form)
                    messages.success(request, 'Email has been sent to ' + data +"'s email address. Please check its inbox to continue reseting password.")
                    return result
                result = self.form_invalid(form)
                messages.error(request, 'This username does not exist in the system.')
                return result
            messages.error(request, 'Invalid Input')
            return self.form_invalid(form)
        
class PasswordResetConfirmView(FormView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "registration/password_reset_email.html"
    success_url = '/admin/'
    form_class = SetPasswordForm

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        UserModel = get_user_model()
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password= form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset.')
                return self.form_valid(form)
            else:
                messages.error(request, 'Password reset has not been unsuccessful.')
                return self.form_invalid(form)
        else:
            messages.error(request,'The reset password link is no longer valid.')
            return self.form_invalid(form)
                    
                    
class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()#raw("select * from api_mall ")
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
        
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
             
   
    
@api_view(['GET'])
def current_product(request):
    product = request.product
    serializer = ProductSerializer(request.product)
    return Response({
        'p_name': product.p_name,
        'id': product.id,
        'response': serializer.data
    })
   
    
@api_view(['GET', 'PUT', 'DELETE'])
def User_detail(request, pk):
    """
    Retrieve, update or delete a code User.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        user1 = UserProfile.objects.get(pk = request.user.pk)
        rs = {'id': user.id,'username':user.username,'email': user.email,'full_name':user1.full_name, 'address':user1.address, 'phone_number':user1.phone_number}
        re1 ={'status':200,'response':rs,'msg':"user successfully displayed"}
        return Response(re1)
        #return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            user1 = UserProfile.objects.get(pk = request.user.pk)
            rs = {'id': user.id,'username':user.username,'email': user.email,'full_name':user1.full_name, 'address':user1.address, 'phone_number':user1.phone_number}
            re1 ={'status':200,'response':rs,'msg':"user information successfully updated"}
            return Response(re1)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE']) 
def Product_view(request, pk):
    """
    Retrieve product information
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(ststus=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        #user1 = UserProfile.objects.get(pk = request.user.pk)
        #rs = {'id': user.id,'username':user.username,'email': user.email,'full_name':user1.full_name, 'address':user1.address, 'phone_number':user1.phone_number}
        re1 ={'status': 200, 'response':serializer.data, 'msg':"product successfully displayed"}
        return Response(re1)

  
@api_view(['GET'])
def Shop_details_view(request, pk):
    """
    Retrieve shop information
    """
    try:
        shop = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        return Response(ststus=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ShopSerializer(shop)
        re1 ={'status': 200, 'response':serializer.data, 'msg':"shop successfully displayed"}
        return Response(re1)
