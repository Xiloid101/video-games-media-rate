# Generated by Django 4.2 on 2023-04-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameData', '0006_videogame_rename_user_articledata_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
