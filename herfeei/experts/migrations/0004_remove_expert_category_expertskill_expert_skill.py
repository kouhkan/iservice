# Generated by Django 4.2 on 2024-01-22 10:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('experts', '0003_alter_warranty_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expert',
            name='category',
        ),
        migrations.CreateModel(
            name='ExpertSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='services.servicecategory')),
                ('expert', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='expert', to='experts.expert')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='expert',
            name='skill',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='expert_skill', to='experts.expertskill'),
            preserve_default=False,
        ),
    ]