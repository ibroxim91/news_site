# Generated by Django 3.0 on 2020-05-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynews', '0005_auto_20200509_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='home',
            field=models.BooleanField(default=False, verbose_name='Bosh saxifaga'),
        ),
    ]
