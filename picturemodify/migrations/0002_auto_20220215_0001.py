# Generated by Django 3.2.8 on 2022-02-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picturemodify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='picture',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
