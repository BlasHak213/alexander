# Generated by Django 5.0.3 on 2024-03-19 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fan_site', '0003_alter_ad_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='adresponse',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='adresponse',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='fan_site.ad'),
        ),
    ]
