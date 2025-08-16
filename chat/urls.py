from django.urls import path
from . import views  # імпортуємо views з цього ж додатку

urlpatterns = [
    path('', views.index, name='chat_index'),  # головна сторінка чату
]
