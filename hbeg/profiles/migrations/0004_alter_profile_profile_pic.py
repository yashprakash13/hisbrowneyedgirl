# Generated by Django 3.2.3 on 2021-05-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/default_profile_picture.png', null=True, upload_to='static/images/profiles'),
        ),
    ]
