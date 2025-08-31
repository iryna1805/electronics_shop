from django.contrib import admin
from .models import Message

#admin.site.register(Message)


@admin.register(Message)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'created_at')