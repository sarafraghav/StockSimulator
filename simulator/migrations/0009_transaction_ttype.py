# Generated by Django 3.2.7 on 2021-10-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0008_holdings_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='ttype',
            field=models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], default='BUY', max_length=100),
            preserve_default=False,
        ),
    ]