# Generated by Django 2.0.4 on 2018-05-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0011_auto_20180522_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
