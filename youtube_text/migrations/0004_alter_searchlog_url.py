# Generated by Django 3.2 on 2021-11-23 06:05

from django.db import migrations, models
import youtube_text.validator


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_text', '0003_alter_searchlog_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchlog',
            name='url',
            field=models.CharField(max_length=500, validators=[youtube_text.validator.validate_url], verbose_name='URL'),
        ),
    ]
