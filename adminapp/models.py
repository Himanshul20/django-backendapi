from random import choices
from django.db import models
from product.models import Main_category,Sub_category,Child_category
from colorfield.fields import ColorField
# Create your models here.

Withdraw_Options = (
        ('Paypal', 'Paypal'),
        ('Skrill', 'Skrill'),
        ('Payoneer','Payoneer'),
        ('Bank','Bank')
    )
class Admin_Add_Product(models.Model):
   
    category = models.ForeignKey(Main_category,  on_delete=models.CASCADE,null=True,blank=True)
    subcategory = models.ForeignKey(Sub_category, on_delete=models.CASCADE,null=True,blank=True)
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
    
    class Meta:
        db_table = "Add_Product"

    

class Product_Size(models.Model):
    product = models.ForeignKey(Admin_Add_Product,on_delete=models.CASCADE)
    Size_name=models.CharField(max_length=200,null=True,blank=True)
    Size_qty=models.IntegerField(null=True,blank=True)
    Size_Price=models.IntegerField(null=True,blank=True)

class Product_Colors(models.Model):
    product = models.ForeignKey(Admin_Add_Product,on_delete=models.CASCADE)
    Product_Colors=ColorField(null=True,blank=True)

class Product_Whole_sell(models.Model):
    product = models.ForeignKey(Admin_Add_Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=True,blank=True)
    discount_perc=models.IntegerField(null=True,blank=True)


    

class Feature_tags(models.Model):
    product = models.ForeignKey(Admin_Add_Product,on_delete=models.CASCADE)
    Feature_tags=models.CharField(max_length=500,null=True,blank=True)
    color=ColorField(null=True,blank=True)

class Product_Images(models.Model):
    product = models.ForeignKey(Admin_Add_Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="Gallery/")
    

class AdminServices(models.Model):
    Title = models.CharField(max_length=100,null=True,blank=True)
    Current_Featured_Image = models.ImageField(upload_to ='Media/services', default="",null=True,blank=True)
    Description = models.TextField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class AdminSocialLinks(models.Model):
    facebook=models.CharField(max_length=500,null=True,blank=True)
    is_active_fb=models.BooleanField(default="False")
    google_plus=models.CharField(max_length=500,null=True,blank=True)
    is_active_google_plus=models.BooleanField(default="False")
    twitter=models.CharField(max_length=500,null=True,blank=True)
    is_active_twitter=models.BooleanField(default="False")
    linkedin=models.CharField(max_length=500,null=True,blank=True)
    is_active_linkedin=models.BooleanField(default="False")


class AdminWithdrawals(models.Model):

    
    Withdraw_Method = models.CharField(choices=Withdraw_Options,max_length=100,null=True,blank=True)
    Withdraw_Amount = models.CharField(max_length=100,null=True,blank=True)
    Additional_Reference = models.TextField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
    class Meta:
        db_table = "Admin_Withdrawals"
    
class Admin_Packaging(models.Model):
    Title = models.CharField(max_length=100,null=True,blank=True)
    Subtitle = models.CharField(max_length=100,null=True,blank=True)
    Price = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Admin_Packaging"

class Admin_ShippingMethod(models.Model):
    Title = models.CharField(max_length=100,null=True,blank=True)
    Duration = models.CharField(max_length=100,null=True,blank=True)
    Price = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = "Admin_Shipping_Method"
    

class Loaders(models.Model):

    Status_website_loader = models.BooleanField(null=True,blank=True)
    Status_admin_loader = models.BooleanField(null=True,blank=True)
    Website_Loader=models.ImageField(upload_to ='media/Loader/',null=True,blank=True)
    Admin_Loader=models.ImageField(upload_to ='media/Loader/',null=True,blank=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        db_table = "Loaders"



Payment_Status = (
        ('Active', 'Active'),
        ('Unactive', 'Unactive'),
    )

Order_Status = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed','Completed'),
        ('Declined','Declined'),
    )
class Order_Details(models.Model):
    total_product=models.CharField(max_length=1000,null=True,blank=True)
    total_cost=models.CharField(max_length=1000,null=True,blank=True)
    ordered_date=models.DateTimeField(null=True,blank=True)
    status=models.CharField(choices=Order_Status,null=True,blank=True,max_length=1000)
    payment_method=models.CharField(max_length=1000,null=True,blank=True)
    payment_status=models.CharField(choices=Payment_Status,max_length=1000,null=True,blank=True)

    class Meta:
        db_table = "Admin_Order_Details"


    

    
class Order_Pickup_Location(models.Model):
    location=models.CharField(max_length=1000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Order_Pickup_Location"

class Footer_Content(models.Model):
    footer_text=models.CharField(max_length=1000,null=True,blank=True)
    copyright_text=models.CharField(max_length=1000,null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Footer_Content"
    
class Popup_Banner(models.Model):
    is_active=models.BooleanField(null=True,blank=True)
    background_image=models.ImageField(upload_to='media/banner',null=True,blank=True)
    popup_title=models.CharField(max_length=1000,null=True,blank=True)
    popup_text=models.TextField(max_length=10000,null=True,blank=True)

    class Meta:
        db_table="Popup_Banner"
    
class Error_Banner(models.Model):
    image=models.ImageField(upload_to="media/banner",null=True,blank=True)

    class Meta:
        db_table="Error_Banner"
    
class Admin_Partners(models.Model):
    image=models.ImageField(upload_to="media/partners",null=True,blank=True)
    link=models.CharField(max_length=1000,null=True,blank=True)

    class Meta:
        db_table="Partners"
    
class Admin_Reviews(models.Model):
    title=models.CharField(max_length=1000,null=True,blank=True)
    subtitle=models.CharField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to="media/reviews",null=True,blank=True)
    description=models.TextField(max_length=1000,null=True,blank=True)

    class Meta:
        db_table="Admin_Reviews"

Role=(
    ('Manager','Manager'),
    ('Moderator','Moderator'),
    ('Staff','Staff')
)
class Admin_Staff(models.Model):
    Staff_Profile_Image = models.ImageField(upload_to ='media/staff', default="",null=True,blank=True)
    Name = models.CharField(max_length=500,null=True,blank=True)
    Email = models.EmailField(max_length=2540, null=True,blank=True)
    Phone=models.CharField(max_length=1000,null=True,blank=True)
    Role=models.CharField(choices=Role,max_length=1000,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table="Admin_Staff"
    
class Website_Contents(models.Model):
    Website_Title=models.CharField(max_length=1000,null=True,blank=True)
    wholesale_max_qty=models.IntegerField(null=True,blank=True)
    theme_color=ColorField(null=True,blank=True)
    footer_color=ColorField(null=True,blank=True) 
    copyright_color=ColorField(null=True,blank=True)

    class Meta:
        db_table="Website_Contents"
    
class Website_maintainence(models.Model):
    status=models.BooleanField(null=True,blank=True,default=True)
    maintainence_text=models.CharField(null=True,blank=True,max_length=1000)

    class Meta:
        db_table="Website_Maintainence"
    
class Affiliate_Information(models.Model):
    status=models.BooleanField(default="True",null=True,blank=True)
    Affilate_Bonus=models.CharField(max_length=500,null=True,blank=True)
    image=models.ImageField(upload_to="media/affiliate",null=True,blank=True)

    class Meta:
        db_table="Affiliate_Info"