# Generated by Django 2.0.4 on 2018-05-23 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0019_categorys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorys',
            name='category',
        ),
        migrations.AddField(
            model_name='categorys',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='video',
            name='cat_list',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='video.Categorys'),
        ),
    ]
