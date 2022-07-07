from django.urls import path
from . import views

urlpatterns=[
    
    path('disputes/', views.Customer_Dispute_List.as_view()),
    path('disputes', views.Customer_Dispute_CreateView.as_view()),
    path('disputes/<int:pk>', views.Customer_DisputeView.as_view()),
    path('tickets/', views.Customer_Tickets_List.as_view()),
    path('tickets', views.Customer_Tickets_CreateView.as_view()),
    path('tickets/<int:pk>', views.Customer_TicketsView.as_view()),
    path('withdrawals/', views.Customer_Withdraw_List.as_view()),
    path('withdrawals', views.Customer_Withdraw_CreateView.as_view()),
    path('withdrawals/<int:pk>', views.CustomerWithdrawView.as_view()),
    path('messages/', views.Customer_Messages_List.as_view()),
    path('messages', views.Customer_Messages_CreateView.as_view()),
    path('messages/<int:pk>', views.Customer_MessagesView.as_view()),

]