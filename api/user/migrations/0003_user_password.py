# Generated by Django 3.2.9 on 2021-11-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=50),
        ),
    ]