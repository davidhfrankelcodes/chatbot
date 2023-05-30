from django.contrib import admin
from .models import ChatBot, Conversation, Message

admin.site.register(ChatBot)
admin.site.register(Conversation)
admin.site.register(Message)
