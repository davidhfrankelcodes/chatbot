from django.contrib.auth.models import Group, Permission
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


@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    create_user_groups(sender, **kwargs)
