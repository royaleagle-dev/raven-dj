# Generated by Django 2.2.17 on 2020-12-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201220_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verification_code',
            field=models.CharField(default='', max_length=255),
        ),
    ]
