# web/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View
from django.views.generic.edit import FormMixin, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django import forms
from .models import ChatBot, Conversation, Message

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate
from langchain.schema import HumanMessage
chat = ChatOpenAI(temperature=0)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)


class BotListView(ListView):
    model = ChatBot
    template_name = 'bot_list.html'

class ConversationListView(ListView):
    model = Conversation
    template_name = 'conversation_list.html'

    def get_queryset(self):
        self.bot = get_object_or_404(ChatBot, id=self.kwargs['bot_id'])
        return Conversation.objects.filter(chatbot=self.bot)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']

class NewConversationView(View):
    def get(self, request, *args, **kwargs):
        bot_id = self.kwargs['bot_id']
        bot = get_object_or_404(ChatBot, id=bot_id)
        new_conversation = Conversation.objects.create(
            user=request.user,
            chatbot=bot,
        )
        return redirect('chat', bot_id=bot_id, conversation_id=new_conversation.id)
    
class ConversationDeleteView(DeleteView):
    model = Conversation
    template_name = 'conversation_confirm_delete.html'

    def get_success_url(self):
        return reverse('conversation_list', kwargs={'bot_id': self.object.chatbot.id})
    
class ChatView(FormMixin, ListView):
    model = Message
    form_class = MessageForm
    template_name = 'chat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chat_name'] = self.conversation
        return context
    
    def get_queryset(self):
        self.conversation = get_object_or_404(Conversation, id=self.kwargs['conversation_id'])
        return Message.objects.filter(conversation=self.conversation)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.conversation = get_object_or_404(Conversation, id=self.kwargs['conversation_id'])
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.conversation = self.conversation
        form.instance.sender = self.request.user
        form.save()

        # Generate a response from the bot
        message_content = form.instance.text
        human_message = HumanMessage(content=message_content)

        # Ensure that the conversation's memory is not None
        memory = self.conversation.get_memory()

        # Update the conversation's memory with the user's message
        memory.chat_memory.add_user_message(message_content)

        # Generate the bot's response based on the conversation history
        bot_message_content = chat(memory.chat_memory.messages).content

        # Add the bot's response to the conversation's memory
        memory.chat_memory.add_ai_message(bot_message_content)
        
        # Save the updated memory back to the conversation
        self.conversation.set_memory(memory)
        self.conversation.save()

        # Save the bot's response
        bot_message = Message.objects.create(
            conversation=self.conversation,
            chatbot=self.conversation.chatbot,
            text=bot_message_content,
        )

        return JsonResponse({
            'user_message': form.instance.text,
            'bot_message': bot_message.text,
        })