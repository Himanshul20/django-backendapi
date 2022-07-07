from django.urls import path, include
from django.conf.urls import url
from .views import (  Admin_Coupon_List, Admin_Slider_List, AdminCouponCreateView, AdminCouponView, AdminSlidersCreateView, AdminSlidersView, CustomerlistView, CustomersView,VendorlistView, LoginView,RegisterView,  UserDetailView, Vendor_subs_List, VendorListView, VendorSubsCreateView, VendorSubsView, SendOtpView,ResetPasswordOtpView,VerifyOtp,Admin_Sliders_list, logout_view)

urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('reset-password-otp', ResetPasswordOtpView.as_view()),
    path('verify-otp', VerifyOtp.as_view()),
    path('user-detail', UserDetailView.as_view()),
    path('logout',logout_view),
    path('customer',CustomersView.as_view()),
    # path('customer/',CustomerListView.as_view()),
    path('customer/<int:pk>',CustomerlistView.as_view()),
    path('vendor-subscription/', Vendor_subs_List.as_view()),
    path('vendor-subscription', VendorSubsCreateView.as_view()),
    path('vendor-subscription/<int:pk>', VendorSubsView.as_view()),
    path('admin-coupon/', Admin_Coupon_List.as_view()),
    path('admin-coupon', AdminCouponCreateView.as_view()),
    path('admin-coupon/<int:pk>', AdminCouponView.as_view()),
    path('vendor',VendorListView.as_view()),
    path('vendor/<int:pk>',VendorlistView.as_view()),
    path('sliders', AdminSlidersCreateView.as_view()),
    path('sliders/', Admin_Slider_List.as_view()),
    path('slider', Admin_Sliders_list.as_view()),
    path('sliders/<int:pk>', AdminSlidersView.as_view()),
    path('send-otp', SendOtpView.as_view()),
    
    
    
    
    
   
    
    # path('reset-password', ResetPasswordView.as_view()),
]