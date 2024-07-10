from django.urls import path
from .views import send_card_info, save_user_credentials

urlpatterns = [
    path('send_card/', send_card_info, name='send_card_info'),
  
    path('save_user_credentials/', save_user_credentials, name='save_user_credentials'),
] 