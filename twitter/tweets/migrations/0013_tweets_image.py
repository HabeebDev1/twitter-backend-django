# Generated by Django 3.1.7 on 2022-02-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0012_auto_20211104_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='image',
            field=models.ImageField(null=True, upload_to='tweetsimages'),
        ),
    ]
