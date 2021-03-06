# Generated by Django 3.0.7 on 2020-06-19 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='linkedCase',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='step',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Subcription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_inProgress', models.BooleanField(default=False)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Case')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
