# Generated by Django 3.2.8 on 2021-11-15 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_auto_20211115_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercisegroup',
            old_name='username',
            new_name='user',
        ),
    ]
