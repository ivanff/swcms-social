# Generated by Django 2.0.2 on 2018-02-14 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='description',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='keywords',
            new_name='keys',
        ),
    ]
