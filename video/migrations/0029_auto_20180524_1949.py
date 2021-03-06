# Generated by Django 2.0.4 on 2018-05-24 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0028_video_uploader_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='Uploader_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='cat_list',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='video.Categorys'),
        ),
        migrations.AlterField(
            model_name='video',
            name='channel_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='video.Channel'),
        ),
    ]
