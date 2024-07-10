from rest_framework import serializers
from .models import CardInfo, UserCredentials

class CardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfo
        exclude = ['id']

class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredentials
        fields = '__all__'
