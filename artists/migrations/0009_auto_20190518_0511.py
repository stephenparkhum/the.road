# Generated by Django 2.2.1 on 2019-05-18 05:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0008_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='signup_Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
