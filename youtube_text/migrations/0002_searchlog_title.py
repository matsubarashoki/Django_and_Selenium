# Generated by Django 3.2 on 2021-11-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_text', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchlog',
            name='title',
            field=models.CharField(default='動画タイトル', max_length=200, verbose_name='タイトル'),
        ),
    ]
