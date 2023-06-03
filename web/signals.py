# signals.py
from django.contrib.auth.models import Group, Permission
from web.models import ChatBot
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver


def create_user_groups(sender, **kwargs):
    groups = [
        {
            'name': 'Chat User',
            'permissions': [
                'web.view_chatbot',
                'web.view_conversation',
                'web.add_conversation',
                'web.change_conversation',
                'web.delete_conversation',
                'web.view_message',
                'web.change_message',
                'web.add_message',
                'web.delete_message',
            ]
        },
    ]
    
    for group_data in groups:
        group, _ = Group.objects.get_or_create(name=group_data['name'])
        
        for permission_codename in group_data['permissions']:
            app_label, action_model = permission_codename.split('.')
            action, model = action_model.split('_')
            content_type = ContentType.objects.get(app_label=app_label, model=model)
            permission = Permission.objects.get(content_type=content_type, codename=action_model)
            group.permissions.add(permission)


def create_default_chatbots(sender, **kwargs):
    default_chatbots = [
        {
            'name': 'chatbot01',
            'system_message_prompt': 'You are a helpful assistant.',
        },
        {
            'name': 'stoner-bot',
            'system_message_prompt': 'You are a helpful assistant but you are quite stoned. Your responses inevitably lead to a weed reference.',
        },
        {
            'name': 'grumpy-bot',
            'system_message_prompt': 'You are grumpy-bot. You are a grumpy assistant. You do not want to help and you are grumpy.',
        },
        {
            'name': 'rhyme-bot',
            'system_message_prompt': 'You are rhyme-bot. You are a helpful assistant and all of your responses are delightful rhymes.',
        },
        {
            "name": "yoda-bot",
            "system_message_prompt": "You are yoda-bot. You are a helpful assistant. All of your responses use yoda-speak syntax.",
        }
    ]

    for chatbot_data in default_chatbots:
        ChatBot.objects.get_or_create(**chatbot_data)


@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    create_user_groups(sender, **kwargs)
    create_default_chatbots(sender, **kwargs)
