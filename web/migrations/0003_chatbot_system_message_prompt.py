# 0003_chatbot_system_message_prompt.py
# Generated by Django 4.2.1 on 2023-06-01 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_conversation_memory'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot',
            name='system_message_prompt',
            field=models.CharField(default='You are a helpful assistant.', max_length=500),
        ),
    ]
