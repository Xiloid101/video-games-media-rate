# Generated by Django 4.2 on 2023-04-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameData', '0002_rename_name_articledata_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articledata',
            name='article',
            field=models.TextField(default=''),
        ),
    ]