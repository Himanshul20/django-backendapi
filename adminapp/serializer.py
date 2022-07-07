from rest_framework import serializers
from .models import Admin_Add_Product, Admin_Packaging, Admin_Partners, Admin_Reviews, Admin_ShippingMethod, Admin_Staff, AdminServices, AdminSocialLinks, AdminWithdrawals, Affiliate_Information, Error_Banner, Footer_Content, Loaders, Order_Details, Order_Pickup_Location, Popup_Banner, Website_Contents, Website_maintainence




class Admin_Add_Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Add_Product
        fields = "__all__"
    
class Admin_withdraw_Serializer(serializers.ModelSerializer):
    class Meta:
        model =AdminWithdrawals
        fields = "__all__"
    
class Admin_Packaging_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Packaging
        fields = "__all__"

class Admin_Shipping_Method_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_ShippingMethod
        fields = "__all__"

class Admin_Social_Links_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdminSocialLinks
        fields = "__all__"

class Admin_Services_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdminServices
        fields = "__all__"

class Loaders_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Loaders
        #fields = "__all__"
        exclude=('Website_Loader','Status_website_loader')
    
class Website_Loaders_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Loaders
        #fields = "__all__"
        exclude=('Admin_Loader','Status_admin_loader')
    
class Order_Pickup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Pickup_Location
        fields = "__all__"
    
class Footer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Footer_Content
        fields = "__all__"
    
class Popup_Banner_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Popup_Banner
        fields = "__all__"
    
class Error_Banner_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Error_Banner
        fields = "__all__"

class Admin_Partners_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Partners
        fields = "__all__"

class Admin_Reviews_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Reviews
        fields = "__all__"

class Admin_Staff_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Staff
        fields = "__all__"

class Admin_order_details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Details
        fields = "__all__"


class Website_Contents_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Website_Contents
        fields = "__all__"


class Website_Maintainance_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Website_maintainence
        fields = "__all__"


class Affiliate_Information_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliate_Information
        fields = "__all__"
