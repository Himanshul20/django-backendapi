from django.urls import path
from . import views


urlpatterns = [
   
    path('maincategory/', views.Main_category_List.as_view()),
    path('main-category', views.MainCategoryCreateView.as_view()),
    path('main-category/<int:pk>', views.MainCategoryView.as_view()),
    path('subcategory/', views.Sub_category_List.as_view()),
    path('sub-category', views.SubCategoryCreateView.as_view()),
    path('sub-category/<int:pk>', views.SubCategoryView.as_view()),
    path('sub-category-list/<int:id>', views.SubCategoryListView.as_view()),
    path('childcategory/', views.Child_category_List.as_view()),
    path('child-category', views.ChildCategoryCreateView.as_view()),
    path('child-category/<int:pk>', views.ChildCategoryView.as_view()),
    path('child-category-list/<int:id>', views.ChildCategoryListView.as_view()),
    path('products/', views.Add_Product_List.as_view()),
    path('products', views.ProductListView.as_view()),
    path('add-product', views.AddProductCreateView.as_view()),
    path('add-product/<int:pk>', views.AddProductView.as_view()),
    path('settings/', views.SettingsGetView.as_view()),
    
    
   
]