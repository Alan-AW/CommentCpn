# Generated by Django 3.2.5 on 2021-12-19 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='replay',
        ),
    ]