# Generated by Django 4.1.3 on 2022-11-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='songs',
            field=models.ManyToManyField(to='main_app.song'),
        ),
    ]