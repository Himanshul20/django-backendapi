from django.contrib import admin

from customerapp.models import Customer_Disputes, Customer_Messages, Customer_Withdrawal, Customer_tickets

# Register your models here.
admin.site.register(Customer_Disputes)
admin.site.register(Customer_Messages)
admin.site.register(Customer_tickets)
admin.site.register(Customer_Withdrawal)
