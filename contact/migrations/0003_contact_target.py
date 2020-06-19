# Generated by Django 3.0.7 on 2020-06-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200619_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='target',
            field=models.CharField(choices=[('SC', 'Service commercial'), ('ST', 'Webmaster'), ('DG', 'Direction'), ('C', 'Candidature'), ('X', 'Default')], default='X', max_length=2),
        ),
    ]
