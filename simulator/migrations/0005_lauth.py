# Generated by Django 3.2.7 on 2021-10-18 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simulator', '0004_auto_20211018_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='lauth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulator.league')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
