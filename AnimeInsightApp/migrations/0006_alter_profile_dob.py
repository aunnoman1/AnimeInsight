# Generated by Django 5.0.4 on 2024-05-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnimeInsightApp', '0005_favgenres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
