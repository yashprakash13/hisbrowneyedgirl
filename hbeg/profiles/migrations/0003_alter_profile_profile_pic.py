# Generated by Django 3.2.4 on 2021-06-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profiles/default_profile_picture.png', null=True, upload_to='profiles'),
        ),
    ]
