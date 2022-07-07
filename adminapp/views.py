from ast import Is
from django.shortcuts import render

from utils.permissions import IsAdmin
from .models import Admin_Add_Product, Admin_Packaging, Admin_Partners, Admin_Reviews, Admin_ShippingMethod, Admin_Staff, AdminServices, AdminSocialLinks,AdminWithdrawals, Affiliate_Information, Error_Banner, Footer_Content, Loaders, Order_Details, Order_Pickup_Location, Popup_Banner, Website_Contents, Website_maintainence
from .serializer import Admin_Add_Product_Serializer, Admin_Partners_Serializer, Admin_Reviews_Serializer,Admin_Social_Links_Serializer, Admin_Staff_Serializer, Admin_order_details_Serializer,Admin_withdraw_Serializer,Admin_Packaging_Serializer,Admin_Shipping_Method_Serializer,Admin_Services_Serializer, Affiliate_Information_Serializer, Error_Banner_Serializer, Footer_Serializer, Loaders_Serializer, Order_Pickup_Serializer, Popup_Banner_Serializer, Website_Contents_Serializer, Website_Loaders_Serializer, Website_Maintainance_Serializer
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import  status
from rest_framework import permissions
from rest_framework.generics import *
from rest_framework.views import *
from django.db.models import Count
from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from adminapp.filters import PROJECT_PARAMETERS
from adminapp.pagination import CustomPagination
# Create your views here.


class Order_status_countView(ListAPIView):
    
    queryset=Order_Details.objects.filter(status='Pending')
    
    serializer_class = Admin_order_details_Serializer
    
    


class Add_Product_List(ListAPIView):
    queryset = Admin_Add_Product.objects.all()
    serializer_class = Admin_Add_Product_Serializer


@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Add_Product'], manual_parameters=PROJECT_PARAMETERS))
class AddProductListView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    serializer_class = Admin_Add_Product_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Admin_Add_Product.objects.filter(is_active=True)
        if search:
            users = Admin_Add_Product.objects.filter(is_active=True,Name__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page)  

class AddProductCreateView(GenericAPIView):
    serializer_class = Admin_Add_Product_Serializer
    permission_classes = (permissions.IsAuthenticated, IsAdmin)

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AddProductView(GenericAPIView):

    serializer_class = Admin_Add_Product_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Add_Product.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None):
        try:
            instace = Admin_Add_Product.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Add_Product.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class Admin_Services_List(ListAPIView):
    queryset =AdminServices.objects.all()
    serializer_class = Admin_Services_Serializer

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Admin_Services'], manual_parameters=PROJECT_PARAMETERS))
class AdminServicesListView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    serializer_class = Admin_Services_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = AdminServices.objects.filter(is_active=True)
        if search:
            users = AdminServices.objects.filter(is_active=True,Title__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 




class AdminServicesCreateView(GenericAPIView):
    serializer_class = Admin_Services_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AdminServicesView(GenericAPIView):

    serializer_class = Admin_Services_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=AdminServices.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = AdminServices.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=AdminServices.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
 #################       
class Admin_Social_Links_List(ListAPIView):
    queryset =AdminSocialLinks.objects.all()
    serializer_class = Admin_Social_Links_Serializer

class AdminSocialLinksCreateView(GenericAPIView):
    serializer_class = Admin_Social_Links_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
###############

class Admin_Packaging_List(ListAPIView):
    queryset =Admin_Packaging.objects.all()
    serializer_class = Admin_Packaging_Serializer

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Admin_Packaging'], manual_parameters=PROJECT_PARAMETERS))
class AdminPackagingListView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    serializer_class = Admin_Packaging_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Admin_Packaging.objects.filter(is_active=True)
        if search:
            users = Admin_Packaging.objects.filter(is_active=True,Title__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 


class AdminPackagingCreateView(GenericAPIView):
    serializer_class = Admin_Packaging_Serializer
    permission_classes = (permissions.IsAuthenticated, IsAdmin)

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AdminPackagingView(GenericAPIView):

    serializer_class = Admin_Packaging_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Packaging.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Admin_Packaging.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Packaging.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)



#######################
class Admin_Shipping_Method_List(ListAPIView):
    queryset =Admin_ShippingMethod.objects.all()
    serializer_class = Admin_Shipping_Method_Serializer

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Admin_Shipping'], manual_parameters=PROJECT_PARAMETERS))
class AdminShippingListView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    serializer_class = Admin_Shipping_Method_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Admin_ShippingMethod.objects.filter(is_active=True)
        if search:
            users = Admin_ShippingMethod.objects.filter(is_active=True,Title__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 


class AdminShippingMethodCreateView(GenericAPIView):
    serializer_class = Admin_Shipping_Method_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AdminShippingMethodView(GenericAPIView):

    serializer_class = Admin_Shipping_Method_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_ShippingMethod.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Admin_ShippingMethod.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_ShippingMethod.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
##################
class Admin_Withdrawals_List(ListAPIView):
    queryset =AdminWithdrawals.objects.all()
    serializer_class = Admin_withdraw_Serializer




class AdminWithdrawCreateView(GenericAPIView):
    serializer_class = Admin_withdraw_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AdminWithdrawView(GenericAPIView):

    serializer_class = Admin_withdraw_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=AdminWithdrawals.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = AdminWithdrawals.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=AdminWithdrawals.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
##############
class WebsiteLoaderView(GenericAPIView):
   
    serializer_class =Website_Loaders_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )


    def get(self,request):
        try:
            serializer = self.serializer_class(instance=Loaders.objects.first())
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            serializer = self.serializer_class(instance=Loaders.objects.first(),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

        
class WebsiteLoaderCreateView(GenericAPIView):
    serializer_class = Website_Loaders_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)


class LoaderView(GenericAPIView):
   
    serializer_class = Loaders_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )


    def get(self,request):
        try:
            serializer = self.serializer_class(instance=Loaders.objects.first())
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            serializer = self.serializer_class(instance=Loaders.objects.first(),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

        
class LoaderCreateView(GenericAPIView):
    serializer_class = Loaders_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
class Order_Pickup_Locations_List(ListAPIView):
    queryset =Order_Pickup_Location.objects.all()
    serializer_class = Order_Pickup_Serializer

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Admin_Order_Pickup_Location'], manual_parameters=PROJECT_PARAMETERS))
class AdminOrderPickupLocationListView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    serializer_class = Order_Pickup_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Order_Pickup_Location.objects.filter(is_active=True)
        if search:
            users = Order_Pickup_Location.objects.filter(is_active=True,location__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 


class OrderPickupLocationCreateView(GenericAPIView):
    serializer_class = Order_Pickup_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class OrderPickupLocationView(GenericAPIView):

    serializer_class = Order_Pickup_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Order_Pickup_Location.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Order_Pickup_Location.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Order_Pickup_Location.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
class Footer_Content_List(ListAPIView):
    queryset =Footer_Content.objects.all()
    serializer_class = Footer_Serializer

        
class FooterContentCreateView(GenericAPIView):
    serializer_class = Footer_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
   
    
    

        
class FooterContentView(GenericAPIView):

    serializer_class = Footer_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

   
    
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Footer_Content.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
class PopupBannerCreateView(GenericAPIView):
    serializer_class = Popup_Banner_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
class PopupBannerView(GenericAPIView):

    serializer_class = Popup_Banner_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Popup_Banner.objects.first())
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Popup_Banner.objects.first(),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
class ErrorBannerCreateView(GenericAPIView):
    serializer_class = Error_Banner_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Admin_Partners'], manual_parameters=PROJECT_PARAMETERS))
class AdminPartnersListView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    serializer_class = Admin_Partners_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Admin_Partners.objects.filter(is_active=True)
        if search:
            users = Admin_Partners.objects.filter(is_active=True,Title__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 
   
class AdminPartnersCreateView(GenericAPIView):
    serializer_class = Admin_Partners_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AdminPartnersView(GenericAPIView):

    serializer_class = Admin_Partners_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Partners.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Admin_Partners.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Partners.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Admin_Reviews'], manual_parameters=PROJECT_PARAMETERS))
class AdminReviewsListView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    serializer_class = Admin_Reviews_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Admin_Reviews.objects.filter(is_active=True)
        if search:
            users = Admin_Reviews.objects.filter(is_active=True,Title__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 
        
class AdminReviewssCreateView(GenericAPIView):
    serializer_class = Admin_Reviews_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AdminReviewsView(GenericAPIView):

    serializer_class =Admin_Reviews_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Reviews.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Admin_Reviews.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Reviews.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
class Admin_Staff_List(ListAPIView):
    queryset =Admin_Staff.objects.all()
    serializer_class = Admin_Staff_Serializer

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Admin_Staff'], manual_parameters=PROJECT_PARAMETERS))
class AdminStaffListView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    serializer_class = Admin_Staff_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Admin_Staff.objects.filter(is_active=True)
        if search:
            users = Admin_Staff.objects.filter(is_active=True,Name__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page) 



class AdminStaffCreateView(GenericAPIView):
    serializer_class = Admin_Staff_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AdminStaffView(GenericAPIView):

    serializer_class = Admin_Staff_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Staff.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Admin_Staff.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Staff.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        

class WebsiteContentView(GenericAPIView):
   
    serializer_class = Website_Contents_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )


    def get(self,request):
        try:
            serializer = self.serializer_class(instance=Website_Contents.objects.first())
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            serializer = self.serializer_class(instance=Website_Contents.objects.first(),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

        
class WebsiteContentcCreateView(GenericAPIView):
    serializer_class = Website_Contents_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
class WebsiteMaintainanceView(GenericAPIView):
   
    serializer_class = Website_Maintainance_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )


    def get(self,request):
        try:
            serializer = self.serializer_class(instance=Website_maintainence.objects.first())
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            serializer = self.serializer_class(instance=Website_maintainence.objects.first(),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

        
class WebsiteMaintainenceCreateView(GenericAPIView):
    serializer_class= Website_Maintainance_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
class AffiliateInfoView(GenericAPIView):
   
    serializer_class = Affiliate_Information_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )


    def get(self,request):
        try:
            serializer = self.serializer_class(instance=Affiliate_Information.objects.first())
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            serializer = self.serializer_class(instance=Affiliate_Information.objects.first(),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

        
class AffiliateInfoCreateView(GenericAPIView):
    serializer_class = Affiliate_Information_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)