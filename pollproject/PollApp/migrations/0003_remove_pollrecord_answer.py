# Generated by Django 4.2.3 on 2023-08-26 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PollApp', '0002_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollrecord',
            name='answer',
        ),
    ]
