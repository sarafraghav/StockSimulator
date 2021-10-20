# Generated by Django 3.2.7 on 2021-10-18 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simulator', '0006_holdings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holdings',
            old_name='buy_price',
            new_name='average_price',
        ),
        migrations.AddField(
            model_name='holdings',
            name='total_investment',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('buy_price', models.IntegerField()),
                ('total_investment', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='simulator.league')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='simulator.stocks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]