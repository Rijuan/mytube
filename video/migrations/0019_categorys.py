# Generated by Django 2.0.4 on 2018-05-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0018_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]
