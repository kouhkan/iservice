# Generated by Django 4.2 on 2024-01-11 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notificationcategory_notificationoption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basenotification',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_cat', to='notifications.notificationcategory'),
        ),
    ]
