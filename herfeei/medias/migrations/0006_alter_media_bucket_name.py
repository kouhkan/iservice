# Generated by Django 4.2 on 2024-01-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('medias', '0005_alter_media_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='bucket_name',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video')], default='image', max_length=32),
        ),
    ]
