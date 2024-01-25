# Generated by Django 4.2 on 2024-01-23 09:42
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='status',
            field=models.CharField(choices=[('ENABLE', 'Enable'),
                                            ('DISABLE', 'Disable')],
                                   default='ENABLE',
                                   max_length=10),
        ),
    ]