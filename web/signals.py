# web/signals.py
from django.apps import apps
from django.contrib.auth.models import Group, Permission
from web.models import ChatBot
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from chatbot.settings import (
    CHAT_USER_GROUP, 
    DEFAULT_CHATBOTS,)

def create_user_groups(sender, **kwargs):
    groups = [
        CHAT_USER_GROUP,
    ]

    for group_data in groups:
        group, _ = Group.objects.get_or_create(name=group_data['name'])

        for permission_codename in group_data['permissions']:
            app_label, action_model = permission_codename.split('.')
            action, model = action_model.split('_')
            content_type = ContentType.objects.get(app_label=app_label, model=model)
            permission, created = Permission.objects.get_or_create(
                content_type=content_type, 
                codename=action_model,
                defaults={'name': f'Can {action} {model}'}
            )
            group.permissions.add(permission)


def create_default_chatbots(sender, **kwargs):
    default_chatbots = DEFAULT_CHATBOTS

    for chatbot_data in default_chatbots:
        ChatBot.objects.get_or_create(**chatbot_data)


@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    if sender.name == 'web':
        create_user_groups(sender, **kwargs)
        create_default_chatbots(sender, **kwargs)
