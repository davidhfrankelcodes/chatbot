# models.py
from django.db import models
from django.contrib.auth.models import User
import pickle
from langchain.memory import ConversationBufferMemory

class ChatBot(models.Model):
    name = models.CharField(max_length=100)
    system_message_prompt = models.CharField(
        max_length=500, default="You are a helpful assistant.")


    def __str__(self):
        return self.name

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatbot = models.ForeignKey(ChatBot, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    memory = models.BinaryField(null=True, blank=True)
    

    def __str__(self):
            return f'Conversation between {self.user.username} and {self.chatbot.name} ({str(self.start_time).split(".")[0]})'
    

    def get_memory(self):
        if self.memory:
            return pickle.loads(self.memory)
        else:
            memory = ConversationBufferMemory()
            self.set_memory(memory)
            self.save()  # Don't forget to save the Conversation instance
            return memory

    def set_memory(self, memory):
        self.memory = pickle.dumps(memory)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    chatbot = models.ForeignKey(ChatBot, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        if self.sender:
            return f'Message from {self.sender.username} at {self.timestamp}'
        else:
            return f'Message from {self.chatbot.name} at {self.timestamp}'
