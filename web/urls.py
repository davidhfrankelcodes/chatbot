# web/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.BotListView.as_view(), name='bot_list'),
    path('bot/<int:bot_id>/', views.ConversationListView.as_view(), name='conversation_list'),
    path('bot/<int:bot_id>/conversation/<int:conversation_id>/', views.ChatView.as_view(), name='chat'),
    path('bot/<int:bot_id>/new_conversation/', views.NewConversationView.as_view(), name='new_conversation'),
    path('bot/<int:bot_id>/conversations/<int:pk>/delete/', views.ConversationDeleteView.as_view(), name='conversation_delete'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
