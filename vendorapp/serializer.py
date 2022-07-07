import email
from rest_framework import serializers
from .models import Vendor
from django.forms import ValidationError
from accounts.models import User
from accounts.serailziers import UserSerialzer
from .models import SettingsBanner,SettingsServices,SettingsSocialLinks, VendorWithdrawals, Vendor_Packaging, Vendor_ShippingMethod
class VendorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User

        # fields = '__all__'
        write_only_fields = ('password', )
        exclude = ('date_joined','last_login','groups','is_active','is_superuser','is_staff','user_permissions',)

    

    def update(self, instance, validated_data):
        if "password" in validated_data:
            from django.contrib.auth.hashers import make_password
            validated_data["password"] = make_password(
                validated_data["password"])
        return super().update(instance, validated_data)

    def create(self, validated_data):
        if  User.objects.filter(email__iexact=validated_data['email']).exists():
            raise ValidationError("Email exist with this email")
        user = super().create(validated_data)
        if validated_data['password']:
            user.set_password(validated_data['password'])
        user.save()
        return user
class Social_Links_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsSocialLinks
        fields = "__all__"




class Services_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsServices
        fields = "__all__"
    
class Banner_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsBanner
        fields = "__all__"
class withdraw_Serializer(serializers.ModelSerializer):
    class Meta:
        model = VendorWithdrawals
        fields = "__all__"
    
class Packaging_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_Packaging
        fields = "__all__"
class Shipping_Method_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_ShippingMethod
        fields = "__all__"