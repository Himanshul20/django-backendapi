from django.shortcuts import render
from .serializer import Customer_withdraw_Serializer,Customer_disputes_Serializer,Customer_tickets_Serializer,Customer_Messages_Serializer, CustomerTicketSerailizer
from rest_framework.generics import ListAPIView, GenericAPIView
from .models import Customer_Messages,Customer_tickets,Customer_Disputes,Customer_Withdrawal
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import  status
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail

# Create your views here.



class Customer_Withdraw_List(ListAPIView):
    queryset = Customer_Withdrawal.objects.all()
    serializer_class = Customer_withdraw_Serializer

class Customer_Withdraw_CreateView(GenericAPIView):
    serializer_class = Customer_withdraw_Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
class CustomerWithdrawView(GenericAPIView):

    serializer_class = Customer_withdraw_Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Customer_Withdrawal.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Customer_Withdrawal.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Customer_Withdrawal.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
class Customer_Messages_List(ListAPIView):
    queryset =Customer_Messages.objects.all()
    serializer_class = Customer_Messages_Serializer

class Customer_Messages_CreateView(GenericAPIView):
    serializer_class = Customer_Messages_Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            subject = Customer_Messages.objects.get('Subject')
            
            message = Customer_Messages.objects.get('Your_Message')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            #send_mail(subject, message, email_from, recipient_list) 
            
            
            email = EmailMessage(subject=subject, body=message, from_email=email_from, to=recipient_list)
            email.send()
           
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
class Customer_MessagesView(GenericAPIView):

    serializer_class = Customer_Messages_Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Customer_Messages.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Customer_Messages.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Customer_Messages.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
class Customer_Tickets_List(ListAPIView):
    queryset = Customer_tickets.objects.all()
    serializer_class = Customer_tickets_Serializer

class Customer_Tickets_CreateView(GenericAPIView):
    serializer_class = CustomerTicketSerailizer
    #permission_classes = (permissions.IsAuthenticated, )

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class Customer_TicketsView(GenericAPIView):

    serializer_class = Customer_tickets_Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Customer_tickets.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Customer_tickets.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Customer_tickets.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
class Customer_Dispute_List(ListAPIView):
    queryset = Customer_Disputes.objects.all()
    serializer_class = Customer_disputes_Serializer

class Customer_Dispute_CreateView(GenericAPIView):
    serializer_class = Customer_disputes_Serializer
    
    permission_classes = (permissions.IsAuthenticated, )

    def post(self,request):
        try:
            
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
         
            
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class Customer_DisputeView(GenericAPIView):

    serializer_class = Customer_disputes_Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Customer_Disputes.objects.get(id=pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        try:
            instace = Customer_Disputes.objects.get(id=pk)
            instace.delete()
            return Response("Deleted success",status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None):
        try:
            serializer = self.serializer_class(instance=Customer_Disputes.objects.get(id=pk),partial=True,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)