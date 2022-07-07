from django.urls import path
from . import views


urlpatterns=[
    path('products/', views.Add_Product_List.as_view()),
    path('products',views.AddProductListView.as_view()),
    path('add-product', views.AddProductCreateView.as_view()),
    path('add-product/<int:pk>', views.AddProductView.as_view()),
    path('services/', views.Admin_Services_List.as_view()),
    path('service',views.AdminServicesListView.as_view()),
    path('services', views.AdminServicesCreateView.as_view()),
    path('services/<int:pk>', views.AdminServicesView.as_view()),
    path('social-links/', views.Admin_Social_Links_List.as_view()),
    path('social-links', views.AdminSocialLinksCreateView.as_view()),
    path('withdrawals/', views.Admin_Withdrawals_List.as_view()),
    path('withdrawals/<int:pk>', views.AdminWithdrawView.as_view()),
    path('shipping-method/', views.Admin_Shipping_Method_List.as_view()),
    path('shipping-method/<int:pk>', views.AdminShippingMethodView.as_view()),
    path('packaging/',views.Admin_Packaging_List.as_view()),
    path('packaging/<int:pk>', views.AdminPackagingView.as_view()),
    path('withdrawals', views.AdminWithdrawCreateView.as_view()),
    path('packaging', views.AdminPackagingCreateView.as_view()),
    path('shipping-method', views.AdminShippingMethodCreateView.as_view()),
    path('pickup-location', views.OrderPickupLocationCreateView.as_view()),
    path('pickup-location/', views.Order_Pickup_Locations_List.as_view()),
    path('pickup-location/<int:pk>', views.OrderPickupLocationView.as_view()),
    path('footer-content', views.FooterContentCreateView.as_view()),
    path('footer-content/',views.Footer_Content_List.as_view()),
    path('footer-content/<int:pk>', views.FooterContentView.as_view()),
    path('popupbanner', views.PopupBannerCreateView.as_view()),
    path('popup-banner/<int:pk>', views.PopupBannerView.as_view()),
    path('errorbanner', views.ErrorBannerCreateView.as_view()),
    path('admin-partners', views.AdminPartnersCreateView.as_view()),
    path('admin-partners/<int:pk>', views.AdminPartnersView.as_view()),
    path('admin-reviews', views.AdminReviewssCreateView.as_view()),
    path('admin-reviews/<int:pk>', views.AdminReviewsView.as_view()),

    path('admin-staff', views.AdminStaffCreateView.as_view()),
    path('admin-staff/', views.Admin_Staff_List.as_view()),
    path('admin-staff/<int:pk>', views.AdminStaffView.as_view()),
    
    path('loaders', views.LoaderCreateView.as_view()),
    path('loaders/', views.LoaderView.as_view()),
    path('website-content', views.WebsiteContentcCreateView.as_view()),
    path('website-content/', views.WebsiteContentView.as_view()),
    path('website-maintainence', views.WebsiteMaintainenceCreateView.as_view()),
    path('website-maintainence/', views.WebsiteMaintainanceView.as_view()),
    path('affiliate-info', views.AffiliateInfoCreateView.as_view()),
    path('affiliate-info/', views.AffiliateInfoView.as_view()),

    path('order-count/', views.Order_status_countView.as_view()),
      
    path('website-loaders', views.WebsiteLoaderCreateView.as_view()),
    path('website-loaders/', views.WebsiteLoaderView.as_view()),

    path('staff/', views.AdminStaffListView.as_view()),
    path('partners', views.AdminPartnersListView.as_view()),
    path('reviews', views.AdminReviewsListView.as_view()),
    path('shipping', views.AdminShippingListView.as_view()),
    path('packaging',views.AdminPackagingListView.as_view()),
    path('admin-pickup-location/', views.AdminOrderPickupLocationListView.as_view()),




]