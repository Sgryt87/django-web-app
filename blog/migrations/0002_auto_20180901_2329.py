# Generated by Django 2.1.1 on 2018-09-01 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='date_posted',
        ),
    ]
