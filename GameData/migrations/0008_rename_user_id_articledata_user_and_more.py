# Generated by Django 4.2 on 2023-04-11 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GameData', '0007_alter_videogame_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articledata',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='articledata',
            old_name='videogame_id',
            new_name='videogame',
        ),
    ]
