from django.contrib import admin
from .models import Admin_Add_Product, Admin_Partners, Admin_Reviews, Affiliate_Information, Error_Banner, Footer_Content, Order_Pickup_Location, Popup_Banner,  Product_Images,Product_Colors, Product_Size,Product_Whole_sell, Feature_tags,AdminServices,AdminWithdrawals,AdminSocialLinks,Admin_Packaging,Admin_ShippingMethod, Loaders, Website_Contents, Website_maintainence
# Register your models here.
class GalaryImages(admin.TabularInline):
    model =Product_Images

class Product_Colorsadmin(admin.TabularInline):
    model =Product_Colors

class Product_wholeselladmin(admin.TabularInline):
    model=Product_Whole_sell

class Product_sizeadmin(admin.TabularInline):
    model=Product_Size

class Feature_tagsadmin(admin.TabularInline):
    model=Feature_tags


@admin.register(Admin_Add_Product)
class AddproductAdmin(admin.ModelAdmin):
    inlines = (GalaryImages,Product_Colorsadmin,Product_sizeadmin,Product_wholeselladmin,Feature_tagsadmin)

admin.site.register(AdminServices)
admin.site.register(Admin_Packaging)
admin.site.register(Admin_ShippingMethod)
admin.site.register(AdminWithdrawals)
admin.site.register(AdminSocialLinks)
admin.site.register(Admin_Partners)
admin.site.register(Admin_Reviews)

admin.site.register(Order_Pickup_Location)

@admin.register(Popup_Banner)
class PopupAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Popup_Banner.objects.count()>0:
            return False
        return True
    
@admin.register(Error_Banner)
class ErrorbAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Error_Banner.objects.count()>0:
            return False
        return True
    
@admin.register(Footer_Content)
class FooterContentAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Footer_Content.objects.count()>0:
            return False
        return True
    
@admin.register(Loaders)
class LoadersAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Loaders.objects.count()>0:
            return False
        return True
    
admin.site.register(Website_Contents)
admin.site.register(Website_maintainence)
admin.site.register(Affiliate_Information)