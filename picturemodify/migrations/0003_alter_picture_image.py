# Generated by Django 3.2.8 on 2022-02-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picturemodify', '0002_auto_20220215_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]