# Generated by Django 2.2.1 on 2019-05-18 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0005_auto_20190518_0316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artists',
            old_name='artist_BC_Url',
            new_name='artist_BC_URL',
        ),
        migrations.RenameField(
            model_name='artists',
            old_name='artist_Fb_Url',
            new_name='artist_FB_URL',
        ),
        migrations.RenameField(
            model_name='artists',
            old_name='artist_Ig_Username',
            new_name='artist_IG_Username',
        ),
        migrations.RenameField(
            model_name='artists',
            old_name='artist_Spotify_Url',
            new_name='artist_Spotify_URL',
        ),
    ]