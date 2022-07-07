from django.db import models
from accounts.models import User

# Create your models here.
Country=(
    ('India','India'),
)

Withdraw_Options = (
        ('Paypal', 'Paypal'),
        ('Skrill', 'Skrill'),
        ('Payoneer','Payoneer'),
        ('Bank','Bank')
    )

state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))


class Vendor(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
  

    
class SettingsServices(models.Model):
    Title = models.CharField(max_length=100,null=True,blank=True)
    Current_Featured_Image = models.ImageField(upload_to ='Media/services', default="",null=True,blank=True)
    Description = models.TextField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SettingsBanner(models.Model):
    Current_Banner = models.ImageField(upload_to ='Media/Banner', default="",null=True,blank=True)

class SettingsSocialLinks(models.Model):
    facebook=models.CharField(max_length=500,null=True,blank=True)
    is_active_fb=models.BooleanField(default="False")
    google_plus=models.CharField(max_length=500,null=True,blank=True)
    is_active_google_plus=models.BooleanField(default="False")
    twitter=models.CharField(max_length=500,null=True,blank=True)
    is_active_twitter=models.BooleanField(default="False")
    linkedin=models.CharField(max_length=500,null=True,blank=True)
    is_active_linkedin=models.BooleanField(default="False")


class VendorWithdrawals(models.Model):

    
    Withdraw_Method = models.CharField(choices=Withdraw_Options,max_length=100,null=True,blank=True)
    Withdraw_Amount = models.CharField(max_length=100,null=True,blank=True)
    Additional_Reference = models.TextField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  
   
    
class Vendor_Packaging(models.Model):
    Title = models.CharField(max_length=100,null=True,blank=True)
    Subtitle = models.CharField(max_length=100,null=True,blank=True)
    Price = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

class Vendor_ShippingMethod(models.Model):
    Title = models.CharField(max_length=100,null=True,blank=True)
    Duration = models.CharField(max_length=100,null=True,blank=True)
    Price = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    