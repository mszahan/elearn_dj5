# Generated by Django 5.1.6 on 2025-04-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_content_options_alter_module_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
