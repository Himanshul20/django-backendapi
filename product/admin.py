from pyexpat import model
from django.contrib import admin

from .models import Add_Product, Child_category, Configs, Main_category, Product_Images, Sub_category,Product_Colors, Product_Size,Product_Whole_sell, Feature_tags

# Register your models here.
admin.site.register(Main_category)
admin.site.register(Sub_category)
admin.site.register(Child_category)
# admin.site.register(Add_Product)

# @admin.register(Featured_Image)


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


@admin.register(Add_Product)
class AddproductAdmin(admin.ModelAdmin):
    inlines = (GalaryImages,Product_Colorsadmin,Product_sizeadmin,Product_wholeselladmin,Feature_tagsadmin)

@admin.register(Configs)
class ConfigAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Configs.objects.count()>0:
            return False
        return True
