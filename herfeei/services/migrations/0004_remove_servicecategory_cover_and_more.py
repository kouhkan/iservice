# Generated by Django 4.2 on 2024-01-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_servicecategory_cover_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecategory',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='is_sub_category',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='parent_category',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='weight',
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='depth',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='numchild',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='path',
            field=models.CharField(default=0, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='description',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='title',
            field=models.CharField(db_index=True, max_length=128),
        ),
    ]