# Generated by Django 3.2.7 on 2021-10-18 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0009_transaction_ttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holdings',
            name='total_investment',
        ),
    ]
