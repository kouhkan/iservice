# Generated by Django 4.2 on 2024-01-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('medias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='usage',
            field=models.CharField(
                choices=[('0', 'Admin Avatar'), ('1', 'Expert Avatar'), ('2', 'User Avatar'), ('3', 'Service'),
                         ('4', 'Order')], default='2', max_length=1),
        ),
    ]
