# Generated by Django 2.2.1 on 2019-05-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_Name', models.CharField(max_length=200)),
                ('tour_Name', models.CharField(blank=True, max_length=200)),
                ('tour_Country', models.URLField(blank=True, default='')),
                ('tour_Type', models.CharField(choices=[('Headliner', 'Headliner'), ('Direct Support', 'Direct Support'), ('Opener', 'Opener')], max_length=200)),
                ('start_Date', models.DateField(blank=True, default='')),
                ('end_Date', models.DateField(blank=True, default='')),
                ('additional_Band', models.CharField(max_length=200)),
                ('owner_ID', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
