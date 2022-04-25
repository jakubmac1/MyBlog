# Generated by Django 3.2.5 on 2022-04-22 13:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220422_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 13, 24, 48, 842993, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 13, 24, 48, 842993, tzinfo=utc)),
        ),
    ]