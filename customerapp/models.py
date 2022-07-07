from django.db import models

# Create your models here.
Withdraw_Options = (
        ('Paypal', 'Paypal'),
        ('Skrill', 'Skrill'),
        ('Payoneer','Payoneer'),
        ('Bank','Bank')
    )
class Customer_Withdrawal(models.Model):

    
    Withdraw_Method = models.CharField(choices=Withdraw_Options,max_length=100,null=True,blank=True)
    Withdraw_Amount = models.CharField(max_length=100,null=True,blank=True)
    Withdraw_Account = models.CharField(max_length=100,null=True,blank=True)
    Additional_Reference = models.TextField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
    


class Customer_tickets(models.Model):

    name=models.CharField(max_length=1000,null=True,blank=True)
    Email = models.EmailField(max_length=254,null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Your_Message = models.TextField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

  


class Customer_Messages(models.Model):

    Name = models.CharField(max_length=100,null=True,blank=True)
    Sent = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=254,null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Your_Message = models.TextField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

    
    

class Customer_Disputes(models.Model):

    name=models.CharField(max_length=1000,null=True,blank=True)
    email=models.CharField(max_length=1000,null=True,blank=True)
    Order_Number = models.CharField(max_length=1000,null=True,blank=True)
    Subject = models.CharField(max_length=1000,null=True,blank=True)
    Your_Message = models.TextField(max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


