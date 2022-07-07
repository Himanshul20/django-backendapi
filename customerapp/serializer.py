from .models import Customer_Messages, Customer_tickets,Customer_Withdrawal,Customer_Disputes,Customer_Withdrawal

from rest_framework import serializers
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail


class Customer_withdraw_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Withdrawal
        fields = "__all__"

class Customer_Messages_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Messages
        fields = "__all__"

class Customer_tickets_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_tickets
        fields = "__all__"

class Customer_disputes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Disputes
        fields = "__all__"
    
class CustomerTicketSerailizer(serializers.Serializer):
    email = serializers.EmailField()
    subject=serializers.CharField(max_length=1000)
    message=serializers.CharField(max_length=1000)
    

    def validate(self, attrs):
        email = attrs.get("email")
        subject = attrs.get("subject")
        message = attrs.get("message")
        
        reset = self.context.get('reset')
        if reset :
                Customer_Disputes.objects.get(email=email,subject=subject,message=message)
           
        
        
        subject = [subject,]
        message = 'hii'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        #send_mail(subject, message, email_from, recipient_list) 
        
        
        email = EmailMessage(subject=subject, body=message, from_email=email_from, to=recipient_list)
        email.send()