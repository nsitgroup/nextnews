# Generated by Django 2.2.10 on 2020-05-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='addressseller',
            field=models.CharField(default='adresse vendeur', max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='firstname',
            field=models.CharField(default='vendeur', max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='lastname',
            field=models.CharField(default='vendeur', max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='shopname',
            field=models.CharField(default='boutique vendeur', max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='telephone',
            field=models.CharField(default='7777777777', max_length=30),
        ),
    ]
