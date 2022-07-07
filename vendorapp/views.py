from django.shortcuts import render

from utils.permissions import IsVendor
from .serializer import Packaging_Serializer, VendorSerialzer
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import  status
from accounts.models import User
from .models import SettingsBanner,SettingsSocialLinks,SettingsServices,Vendor_ShippingMethod,VendorWithdrawals,Vendor_Packaging, Vendor
from .serializer import Banner_Serializer, Services_Serializer,Social_Links_Serializer, Shipping_Method_Serializer, Shipping_Method_Serializer,withdraw_Serializer
# Create your views here.



class VendorRegisterView(GenericAPIView):
    serializer_class = VendorSerialzer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        try:
            # user=User.objects.create(name=name,email=email,phone=phone)
            # user.set_password(password)
            # user.save()

            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)



class Social_Links_List(ListAPIView):
    queryset = SettingsSocialLinks.objects.all()
    serializer_class = Social_Links_Serializer

class SocialLinksCreateView(GenericAPIView):
    serializer_class = Social_Links_Serializer
    permission_classes = (permissions.IsAuthenticated,IsVendor )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)


class Services_List(ListAPIView):
    queryset = SettingsServices.objects.all()
    serializer_class = Services_Serializer

class ServicesCreateView(GenericAPIView):
    serializer_class = Services_Serializer
    permission_classes = (permissions.IsAuthenticated,IsVendor )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class ServicesView(GenericAPIView):

    serializer_class = Services_Serializer
    permission_classes = (permissions.IsAuthenticated, IsVendor)

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=SettingsServices.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = SettingsServices.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=SettingsServices.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class Banner_List(ListAPIView):
    queryset = SettingsBanner.objects.all()
    serializer_class = Banner_Serializer

class BannerCreateView(GenericAPIView):
    serializer_class = Banner_Serializer
    permission_classes = (permissions.IsAuthenticated, IsVendor)

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    
class Shipping_Method_List(ListAPIView):
    queryset = Vendor_ShippingMethod.objects.all()
    serializer_class = Shipping_Method_Serializer

class ShippingMethodCreateView(GenericAPIView):
    serializer_class = Shipping_Method_Serializer
    permission_classes = (permissions.IsAuthenticated,IsVendor )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class ShippingMethodView(GenericAPIView):

    serializer_class = Shipping_Method_Serializer
    permission_classes = (permissions.IsAuthenticated, IsVendor)

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Vendor_ShippingMethod.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Vendor_ShippingMethod.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Vendor_ShippingMethod.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
class Packaging_List(ListAPIView):
    queryset = Vendor_Packaging.objects.all()
    serializer_class = Packaging_Serializer

class Packaging_MethodCreateView(GenericAPIView):
    serializer_class = Packaging_Serializer
    permission_classes = (permissions.IsAuthenticated,IsVendor )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
class Packaging_Method_View(GenericAPIView):

    serializer_class = Packaging_Serializer
    permission_classes = (permissions.IsAuthenticated, IsVendor)

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Vendor_Packaging.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Vendor_Packaging.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Vendor_Packaging.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
class Withdrawal_List(ListAPIView):
    queryset = VendorWithdrawals.objects.all()
    serializer_class = withdraw_Serializer

class WithdrawalCreateView(GenericAPIView):
    serializer_class = withdraw_Serializer
    permission_classes = (permissions.IsAuthenticated,IsVendor )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class WithdrawalView(GenericAPIView):

    serializer_class = withdraw_Serializer
    permission_classes = (permissions.IsAuthenticated, IsVendor)

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=VendorWithdrawals.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = VendorWithdrawals.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=VendorWithdrawals.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
