# Generated by Django 2.2.17 on 2020-12-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_invoice_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='trashed',
            field=models.BooleanField(default=False),
        ),
    ]
