# Generated by Django 2.2.17 on 2020-12-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
