# 0002_conversation_memory.py
# Generated by Django 4.2.1 on 2023-05-29 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='memory',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
