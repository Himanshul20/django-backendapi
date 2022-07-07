

# Create your models here.
from distutils.command.upload import upload
from django.db import models
from numpy import product
from colorfield.fields import ColorField
# Create your models here.
# from django.contrib.auth.models import User
CATEGORY_STATUS = (
        ('Active', 'Active'),
        ('Disabled', 'Disabled'),
    )


class Main_category(models.Model):

    Name = models.CharField(max_length=100,null=True,blank=True)
    Slug = models.CharField(max_length=100,null=True,blank=True)
    Status = models.CharField(choices=CATEGORY_STATUS,max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.Name
    class Meta:
        
        db_table="Main_category"


class Sub_category(models.Model):
    category = models.ForeignKey(Main_category,  on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=True,blank=True)
    slug = models.SlugField(max_length=150,null=True,blank=True)
    Status = models.CharField(choices=CATEGORY_STATUS,max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        
        db_table = "Sub_category"
    
        

class Child_category(models.Model):
    category = models.ForeignKey(Main_category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100,null=True,blank=True)
    Slug = models.CharField(max_length=100,null=True,blank=True)
    Status = models.CharField(choices=CATEGORY_STATUS,max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Name
    

    class Meta:
        db_table = "Child_category"

class Add_Product(models.Model):
   
    category = models.ForeignKey(Main_category,  on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    child_category = models.ForeignKey(Child_category, on_delete=models.CASCADE,null=True,blank=True)
    Product_Sku=models.CharField(max_length=1000,default="",null=True,blank=True)
    Name = models.CharField(max_length=300,db_index=True,null=True,blank=True)
    Slug = models.CharField(max_length=300, db_index=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Product_Estimated_Shipping_Time=models.CharField(max_length=200,null=True,blank=True)
    Product_Stock=models.CharField(max_length=1000,default="",null=True,blank=True)
    Product_Description=models.TextField(max_length=1000,default="",null=True,blank=True)
    Product_Buy_Return_Policy=models.TextField(max_length=1000,default="",null=True,blank=True)
    meta_tags=models.CharField(max_length=200,null=True,blank=True)
    meta_description=models.TextField(max_length=1000,null=True,blank=True)
    featured_image=models.ImageField(upload_to="featured_image/",blank=True,null=True)
    youtube_video_url=models.CharField(max_length=300,blank=True,null=True)
    Product_Current_Price=models.CharField(max_length=100,default="",null=True,blank=True)
    Product_Previous_Price=models.CharField(max_length=100,default="",null=True,blank=True)
    
    Tags=models.CharField(max_length=100,default="")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name


    

class Product_Size(models.Model):
    product = models.ForeignKey(Add_Product,on_delete=models.CASCADE)
    Size_name=models.CharField(max_length=200,null=True,blank=True)
    Size_qty=models.IntegerField(null=True,blank=True)
    Size_Price=models.IntegerField(null=True,blank=True)

class Product_Colors(models.Model):
    product = models.ForeignKey(Add_Product,on_delete=models.CASCADE)
    Product_Colors=ColorField(null=True,blank=True)

class Product_Whole_sell(models.Model):
    product = models.ForeignKey(Add_Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=True,blank=True)
    discount_perc=models.IntegerField(null=True,blank=True)


    

class Feature_tags(models.Model):
    product = models.ForeignKey(Add_Product,on_delete=models.CASCADE)
    Feature_tags=models.CharField(max_length=500,null=True,blank=True)
    color=ColorField(null=True,blank=True)

class Product_Images(models.Model):
    product = models.ForeignKey(Add_Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="Gallery/")
    class Meta:
        db_table = "Admin_Add_Product"
    
class Configs(models.Model):
    header_logo=models.ImageField(upload_to ='uploads/', default="" ,blank=True,null=True )
    Footer_logo=models.ImageField(upload_to ='uploads/', default="",blank=True,null=True)
    Invoice_logo=models.ImageField(upload_to ='uploads/', default="",blank=True,null=True)
    Favicon=models.ImageField(upload_to ='uploads/', default="",blank=True,null=True)



  
   