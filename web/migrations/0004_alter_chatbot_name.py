# Generated by Django 4.2.1 on 2023-06-03 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_chatbot_system_message_prompt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbot',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
