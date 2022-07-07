from django.urls import path, include

from accounts.views import RegisterView
from .views import (VendorRegisterView)
from vendorapp import views

urlpatterns = [
   
    path('register', VendorRegisterView.as_view()),
    path('services/', views.Services_List.as_view()),
    path('services/<int:pk>', views.ServicesView.as_view()),
    path('banner/', views.Banner_List.as_view()),
    path('social-links/',views.Social_Links_List.as_view()),
    path('banner', views.BannerCreateView.as_view()),
    path('service', views.ServicesCreateView.as_view()),
    path('social-links', views.SocialLinksCreateView.as_view()),
    path('withdrawals/', views.Withdrawal_List.as_view()),
    path('withdrawals/<int:pk>', views.WithdrawalView.as_view()),
    path('shipping-method/', views.Shipping_Method_List.as_view()),
    path('shipping-method/<int:pk>', views.ShippingMethodView.as_view()),
    path('packaging/',views.Packaging_List.as_view()),
    path('packaging/<int:pk>', views.Packaging_Method_View.as_view()),
    path('withdrawals', views.WithdrawalCreateView.as_view()),
    path('packaging', views.Packaging_MethodCreateView.as_view()),
    path('shipping-method', views.ShippingMethodCreateView.as_view()),
    # path('user-detail', UserDetailView.as_view()),
    
    # path('reset-password', ResetPasswordView.as_view()),
]