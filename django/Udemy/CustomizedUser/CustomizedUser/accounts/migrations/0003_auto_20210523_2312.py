# Generated by Django 3.2 on 2021-05-23 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_schools_students'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schools',
            options={'verbose_name_plural': '学校'},
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name_plural': '生徒'},
        ),
        migrations.RenameField(
            model_name='students',
            old_name='schoole',
            new_name='school',
        ),
    ]
