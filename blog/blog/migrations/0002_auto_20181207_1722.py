# Generated by Django 2.1.4 on 2018-12-07 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creation_date',
            new_name='date',
        ),
    ]