# Generated by Django 3.0.7 on 2020-06-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200628_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='post',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='resume',
            field=models.TextField(blank=True, null=True),
        ),
    ]