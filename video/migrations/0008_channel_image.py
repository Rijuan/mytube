# Generated by Django 2.0.4 on 2018-05-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
