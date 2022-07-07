

from utils.permissions import IsAdmin
from .serailziers import Admin_Slider_Serializer, AuthTokenSerializer, Coupon_Serializer, UserSerialzer, Vendor_subs_Serializer, VendorlistSerialzer, CustomerlistSerialzer,OtpSerailizer
from rest_framework.generics import *
from rest_framework.views import *
from .pagination import CustomPagination
from django.utils.decorators import method_decorator
from .filters import PROJECT_PARAMETERS
from knox.views import LoginView as KnoxLoginView
from rest_framework.generics import GenericAPIView, ListAPIView
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from .models import  Admin_Coupon, Admin_Sliders, User, Vendor_subs
from rest_framework import permissions
from django.contrib.auth import login
from rest_framework import  status
from knox.auth import TokenAuthentication
from django.contrib.auth import logout
from django.core.mail import EmailMessage  
from ast import ExceptHandler
from random import randint
from django.core.mail.backends.smtp import EmailBackend


from django.conf import settings


from django.core.mail import send_mail





class VerifyOtp(GenericAPIView):

    permission_classes = (permissions.AllowAny, )
    serializer_class = OtpSerailizer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data["email"]
        otp = int(request.data["otp"])
        user = User.objects.get(email=email)

        if int(user.otp)==otp:
            user.is_email_verified = True
            #user.otp.delete()  #?? How to handle the otp, Should I set it to null??
            user.save()
            return Response("Verification Successful")
        else:
            return Response("OTP Verification failed",status=status.HTTP_400_BAD_REQUEST)

class SendOtpView(GenericAPIView):
    serializer_class = OtpSerailizer
    permission_classes = (permissions.AllowAny, )

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
       
        return Response(serializer.data,status=status.HTTP_200_OK)
# Create your views here.
class CustomerListView(ListAPIView):
    serializer_class = CustomerlistSerialzer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )
    queryset=User.objects.filter(user_type="Customer")
@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Customers'], manual_parameters=PROJECT_PARAMETERS))
class CustomersView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    serializer_class = CustomerlistSerialzer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = User.objects.filter(is_active=True,user_type="Customer")
        if search:
            users = User.objects.filter(is_active=True,name__contains=search,user_type="Customer")
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page)
    

class CustomerlistView(GenericAPIView):

    serializer_class = CustomerlistSerialzer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )
    

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=User.objects.get(user_type="Customer",id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = User.objects.get(user_type="Customer",id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=User.objects.get(id=pk,user_type="Customer"),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class VendorListView(ListAPIView):
    serializer_class = VendorlistSerialzer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )
    queryset=User.objects.filter(user_type="Vendor") 

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Vendors'], manual_parameters=PROJECT_PARAMETERS))
class VendorListView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = VendorlistSerialzer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = User.objects.filter(is_active=True,user_type="Vendor")
        if search:
            users = User.objects.filter(is_active=True,name__contains=search,user_type="Vendor")
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page)
    

class VendorlistView(GenericAPIView):
    queryset=User.objects.filter(user_type="Vendor")

    serializer_class = VendorlistSerialzer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )
   
    

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=User.objects.get(user_type="Vendor",id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = User.objects.get(user_type="Vendor",id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=User.objects.get(id=pk,user_type="Vendor"),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    



    
   
    
   
    
    
class LoginView(GenericAPIView, KnoxLoginView):
#     '''
#     Function for login
#      '''
    serializer_class = AuthTokenSerializer
    permission_classes = (permissions.AllowAny, )

    

  

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

    def get_post_response_data(self, request, token, instance):

        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token
        }
        if UserSerialzer is not None:
            data["user"] = UserSerialzer(request.user).data
        return data

class RegisterView(GenericAPIView):
    serializer_class = UserSerialzer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        # subject = 'Your accounts need to be verified'
        # message = 'Hi paste the link to verify your account'
        # to_email = [serializer['email']]
        # email = EmailMessage(  
        #                 "hello", message, to=[to_email]  
        #     )  
        # email.send() 
    
        return Response(serializer.data,status=status.HTTP_201_CREATED)




    

class UserDetailView(GenericAPIView):
    serializer_class = UserSerialzer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get(self,request):
        serializer = self.serializer_class(instance=request.user)

        return Response(serializer.data)
    
    def patch(self,request):
        serializer = self.serializer_class(instance=request.user,data=request.data,partial=True)  
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
class ResetPasswordOtpView(GenericAPIView):
    serializer_class = OtpSerailizer
    permission_classes = (permissions.AllowAny, )


    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data,context={'reset':True})
            serializer.is_valid(raise_exception=True)
        
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"{e}",status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(GenericAPIView):
    serializer_class = UserSerialzer
    permission_classes = (permissions.AllowAny, )

    def post(self,request):
        try:
            serializer = self.serializer_class(instance=User.objects.get(email=request.data['email']) ,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"{e}",status=status.HTTP_400_BAD_REQUEST)

def logout_view(request):
    logout(request)


@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Vendor_Subs'], manual_parameters=PROJECT_PARAMETERS))
class Vendor_subs_List(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = Vendor_subs_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Vendor_subs.objects.filter()
        if search:
            users = Vendor_subs.objects.filter(Title__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page)

class VendorSubsCreateView(GenericAPIView):
    serializer_class = Vendor_subs_Serializer
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    
    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class VendorSubsView(GenericAPIView):

    serializer_class = Vendor_subs_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Vendor_subs.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Vendor_subs.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Vendor_subs.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)


@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Admin_Coupons'], manual_parameters=PROJECT_PARAMETERS))
class Admin_Coupon_List(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = Coupon_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Admin_Coupon.objects.filter()
        if search:
            users = Admin_Coupon.objects.filter(Cost__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page)

class AdminCouponCreateView(GenericAPIView):
    serializer_class = Coupon_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )
    
    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class AdminCouponView(GenericAPIView):

    serializer_class = Coupon_Serializer
    permission_classes = (permissions.IsAuthenticated, IsAdmin)

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Coupon.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Admin_Coupon.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Coupon.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)   

        
class AdminSlidersCreateView(GenericAPIView):
    serializer_class = Admin_Slider_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class Admin_Sliders_list(ListAPIView):
    queryset =Admin_Sliders.objects.all()
    serializer_class = Admin_Slider_Serializer
class AdminSlidersView(GenericAPIView):

    serializer_class =Admin_Slider_Serializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Sliders.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Admin_Sliders.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Admin_Sliders.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)     

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Get All your project List",
    tags=['Admin_Sliders'], manual_parameters=PROJECT_PARAMETERS))
class Admin_Slider_List(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = Admin_Slider_Serializer
    pagination_class = CustomPagination()
    

    
    def get(self,request,):
        search = request.GET.get('search',None)

        users = Admin_Sliders.objects.filter()
        if search:
            users = Admin_Sliders.objects.filter(link__contains=search)
            
        serializer = self.serializer_class(instance=users.order_by('-id'),many=True)
        page = self.pagination_class.paginate_queryset( queryset=serializer.data, request=request)

        if page is not None:
            return self.pagination_class.get_paginated_response(page)
        return Response(page)
