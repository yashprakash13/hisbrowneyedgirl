# Generated by Django 3.2.3 on 2021-05-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20210522_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='story',
            field=models.ManyToManyField(blank=True, null=True, to='profiles.Story'),
        ),
    ]
