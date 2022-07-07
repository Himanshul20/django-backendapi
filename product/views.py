from ast import Is
from unicodedata import name
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from uritemplate import partial

from utils.permissions import IsAdmin, IsVendor
from .models import Configs, Main_category, Child_category, Sub_category, Add_Product
from .serializers import  ConfigSerializer, Main_category_Serializer, Sub_category_Serializer, Child_category_Serializer, Add_Product_Serializer,Child_categoryCreateSerializer, Sub_category_CreateSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import  status
from product.pagination import CustomPagination
from product.filters import PROJECT_PARAMETERS
from rest_framework.generics import *
from rest_framework.views import *
from .pagination import CustomPagination
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema



from django.http import HttpResponse
import json
# Create your views here.
@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Main_Category'], manual_parameters=PROJECT_PARAMETERS))
class Main_category_List(APIView):
    permission_classes = (permissions.IsAuthenticated,IsVendor)
    serializer_class = Main_category_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Add_Product.objects.filter(is_active=True)
        if search:
            users = Add_Product.objects.filter(is_active=True,Name__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 

    
    


class MainCategoryCreateView(GenericAPIView):
    serializer_class = Main_category_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )
    

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class MainCategoryView(GenericAPIView):

    serializer_class = Main_category_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin,IsVendor )
    

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Main_category.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Main_category.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Main_category.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Sub_Category'], manual_parameters=PROJECT_PARAMETERS))
class Sub_category_List(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = Sub_category_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Add_Product.objects.filter(is_active=True)
        if search:
            users = Add_Product.objects.filter(is_active=True,name__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 
   



class SubCategoryCreateView(GenericAPIView):
    serializer_class = Sub_category_CreateSerializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)


class SubCategoryView(GenericAPIView):

    serializer_class = Sub_category_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )
    

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Sub_category.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Sub_category.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Sub_category.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class SubCategoryListView(GenericAPIView):
    serializer_class = Sub_category_Serializer
    
    def get(self,request,id=None):
        try:
            serializer = self.serializer_class(instance=Sub_category.objects.filter(category=id,Status="Active"),many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class ChildCategoryListView(GenericAPIView):
    serializer_class = Child_category_Serializer
  
    def get(self,request,id=None):
        try:
            serializer = self.serializer_class(instance=Child_category.objects.filter(sub_category=id,Status="Active"),many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Child_Category'], manual_parameters=PROJECT_PARAMETERS))
class Child_category_List(APIView):
    permission_classes = (permissions.IsAuthenticated,IsVendor)
    serializer_class = Child_category_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Add_Product.objects.filter(is_active=True)
        if search:
            users = Add_Product.objects.filter(is_active=True,Name__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 
    

class ChildCategoryCreateView(GenericAPIView):
    serializer_class = Child_categoryCreateSerializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class ChildCategoryView(GenericAPIView):

    serializer_class = Child_category_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )
    

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Child_category.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Child_category.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Child_category.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class Add_Product_List(ListAPIView):
    queryset = Add_Product.objects.all()
    serializer_class = Add_Product_Serializer

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Products'], manual_parameters=PROJECT_PARAMETERS))
class ProductListView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = Add_Product_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Add_Product.objects.filter(is_active=True)
        if search:
            users = Add_Product.objects.filter(is_active=True,Name__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page)   




class AddProductCreateView(GenericAPIView):
    serializer_class = Add_Product_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin,IsVendor )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AddProductView(GenericAPIView):

    serializer_class = Add_Product_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin,IsVendor )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Add_Product.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Add_Product.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Add_Product.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)



 

class SettingsGetView(GenericAPIView):
   
    serializer_class = ConfigSerializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )


    def get(self):
        try:
            serializer = self.serializer_class(instance=Configs.objects.first())
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            serializer = self.serializer_class(instance=Configs.objects.first(),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)


