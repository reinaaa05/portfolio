# Generated by Django 3.1.7 on 2021-03-18 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_auto_20210318_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatedAt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='作成日')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='diaries.createdat', verbose_name='作成日'),
        ),
    ]
