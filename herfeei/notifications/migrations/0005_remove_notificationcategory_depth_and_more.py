# Generated by Django 4.2 on 2024-01-11 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_alter_basenotification_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationcategory',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='notificationcategory',
            name='numchild',
        ),
        migrations.RemoveField(
            model_name='notificationcategory',
            name='path',
        ),
    ]