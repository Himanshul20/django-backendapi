from unicodedata import category
from django.forms import ValidationError
from rest_framework import serializers
from .models import  Main_category, Sub_category, Child_category, Add_Product,Configs


class Main_category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Main_category
        fields = ['id', 'Name', 'Slug','Status','created_at','updated_at']


class Sub_category_Serializer(serializers.ModelSerializer):
    category=Main_category_Serializer(read_only=True)
    class Meta:
        model = Sub_category
        fields = "__all__"

class Sub_category_CreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sub_category
        fields = "__all__"


class Child_category_Serializer(serializers.ModelSerializer):
    category=Main_category_Serializer(read_only=True)
    sub_category=Sub_category_Serializer(read_only=True)
    class Meta:
        model = Child_category
        fields = "__all__"

class Child_categoryCreateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Child_category
        fields = "__all__"

class Add_Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_Product
        fields = "__all__"

class ConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = Configs
        fields = '__all__'