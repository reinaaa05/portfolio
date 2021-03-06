# Generated by Django 3.2 on 2021-04-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20210331_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='bad',
            field=models.IntegerField(blank=True, null=True, verbose_name='低評価'),
        ),
        migrations.AddField(
            model_name='video',
            name='badtext',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='good',
            field=models.IntegerField(blank=True, null=True, verbose_name='高評価'),
        ),
        migrations.AddField(
            model_name='video',
            name='goodtext',
            field=models.TextField(blank=True, null=True),
        ),
    ]
