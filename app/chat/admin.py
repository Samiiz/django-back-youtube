from django.contrib import admin
from .models import ChatRoom

# Register your models here.
@admin.register(ChatRoom)
class ChatAdmin(admin.ModelAdmin):
    pass