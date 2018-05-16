from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from sorl.thumbnail.shortcuts import get_thumbnail
from django.core.files.base import ContentFile
from PIL import Image
#from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from _io import StringIO


ROLE_CHOICES = (
    ('c1', 'choice1'),
    ('c2', 'choice2'),
    ('c3', 'choice3'),
    ('o', 'other'),
    )
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('o', 'other'),
    )
PTYPE_CHOICES = (
    ('A', 'Avilable'),
    ('NA', 'Not Avilable'),
    ('N', 'New stoke'),
    ('Ol', 'Old stoke'),
    ('O', 'Others'),
    )
SSTATUS_CHOICES = (
    ('O', 'Open'),
    ('C', 'Close'),
    ('S', 'Shifted'),
    ('o', 'Other'),
    )
ESTATUS_CHOICES = (
    ('D', 'on-duty'),
    ('L', 'leave'),
    ('W', 'Weekly off'),
    ('O', 'Other'),
    )

# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
       
    
class Category(models.Model):
    C_name = models.CharField(max_length=255, blank=False, help_text="Enter category name")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.C_name
    
class ProductType(models.Model):
    PT_name = models.CharField(max_length=255, blank=False, help_text="enter Type name")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.PT_name
    
class ShopType(models.Model):
    T_name = models.CharField(max_length=255, blank=False, help_text="enter Type name")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.T_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    #product_id = models.ManyToManyField(Product, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.brand_name
    
class ProductSize(models.Model):
    #product_id = models.ManyToManyField(Product, on_delete=models.CASCADE, primary_key=True)
    size_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.size_name
    
class Color(models.Model):
    #product_id = models.ManyToManyField(Product, on_delete=models.CASCADE, primary_key=True)
    color_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.color_name
    
class Mall(models.Model):
    MName = models.CharField(max_length=255, blank=False, help_text="Enter Mall Name")
    MCategory = models.ManyToManyField(Category, blank=True, verbose_name=("Mall Categories") )
    MAddress = models.CharField(max_length=255, blank=False, help_text="Enter Address of the Mall")
    M_image = models.ImageField(upload_to= 'media/document/product/%Y/%m/%d/',null=True,blank=True)
    thumb_pic = models.ImageField(upload_to = 'mall/thumb/',null=True,blank=True)
    M_Status = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
   
    def delete(self, *args, **kwargs):
        storage, path = self.M_image.storage, self.M_image.path
        storage1, path1 = self.thumb_pic.storage, self.thumb_pic.path
        super(Mall, self).delete(*args, **kwargs)
        storage.delete(path)
        storage1.delete(path1)
        
    def save(self, *args, **kwargs):
        try:
            this = Mall.objects.get(id=self.id)
            self.create_thumbnail()
            if this.M_image != self.M_image:
                this.M_image.delete(save=False)
                this.thumb_pic.delete(save=False)
        except: pass
        super(Mall, self).save(*args, **kwargs)
        
    def create_thumbnail(self):
        if not self.M.image:
            THUMBNAIL_SIZE = (200,200)
            DJANGO_TYPE = self.M_image.file.content_type
            if DJANGO_TYPE == 'image/jpeg':
                PIL_TYPE = 'jpeg'
                FILE_EXTENSION = 'jpg'
            elif DJANGO_TYPE == 'image/png':
                PIL_TYPE = 'png'
                FILE_EXTENSION = 'png'
                image = Image.open(StringIO(self.M_image.read()))
                image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
                temp_handle = StringIO()
                image.save(temp_handle, PIL_TYPE)
                temp_handle.seek(0)
                suf = SimpleUploadedFile(os.path.split(self.M_image.name)[-1],temp_handle.read(), content_type=DJANGO_TYPE)
                self.thumb_pic.save('%s.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

        return 
        
    def __str__(self):
        return self.MName
    
class Product(models.Model):
    P_name = models.CharField(max_length=255, blank=False, help_text="Enter Product Name")
    P_image = models.ImageField(upload_to= 'media/document/product/%Y/%m/%d/')
    p_Cost = models.CharField(max_length=255, blank=False, help_text="Enter Product Cost")
    P_status = models.CharField(max_length=1, choices=PTYPE_CHOICES)
    P_features = models.TextField()
    size = models.ManyToManyField(ProductSize)
    color = models.ManyToManyField(Color)
    Brand = models.ManyToManyField(Brand)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.P_name
    
class Shop(models.Model):
    SName = models.CharField(max_length=255, blank=False, help_text="Enter shop Name")
    SCategory = models.CharField(max_length=255, blank=False, help_text="Enter shop Category")
    Shop_number = models.CharField(max_length=255, blank=False, help_text="Enter shop number")
    Shop_type = ManyToManyField(ShopType, blank=True, verbose_name=("Product type"))
    S_status = models.CharField(max_length=1, choices=SSTATUS_CHOICES)
    Product_type = ManyToManyField(Product, blank=True, verbose_name=("Shop type"))
    Shop_location = models.ForeignKey(Mall, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.SName
    
class Employee(models.Model):
    Emp_name = models.CharField(max_length=255, blank=False, help_text="Enter Employee Name")
    Emp_email = models.EmailField(max_length=255, null=True, blank=True, unique=True, help_text="Enter Email")
    Emp_age = models.CharField(max_length=255, help_text="Enter age")
    Emp_salary = models.CharField(max_length=255, blank=False, help_text="Enter Salary")
    Emp_image = models.ImageField(upload_to= 'media/document/%y/%m/%d/')
    Emp_role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    Emp_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    W_mall = models.ForeignKey(Mall, on_delete=models.CASCADE)
    W_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    Emp_status = models.CharField(max_length=1, choices=ESTATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Emp_Name  
    
class Order(models.Model):
    customer_name = models.CharField(max_length=255, blank=False, help_text="Enter Customer name")
    customer_address = models.TextField()
    Product_name = models.CharField(max_length=255)
    Product_cost = models.CharField(max_length=255)
    Phone_number = models.CharField(max_length=255, blank=False, help_text="enter phone number")
    Order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()
    #Product_Id = models.ManyToManyField()
    #User_Id = models.ManyToManyField()
    
    def __str__(self):
        return self.customer_name
    




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True, related_name="UserProfile")
    full_name = models.CharField(max_length=255, null=True, blank=False, error_messages={'required':"full name is required"})
    address = models.TextField(null=True, blank=True)
    phone_number =models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.full_name
         
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    phone_number =models.CharField(max_length=255, blank=True, null=True)
    
class WishList(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_id
    
class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.product_id
