# Generated by Django 2.2.1 on 2019-05-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20190522_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='venue_Location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
