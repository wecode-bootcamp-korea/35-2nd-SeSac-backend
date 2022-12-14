# Generated by Django 4.0.6 on 2022-08-02 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='location_id',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='posthashtag',
            old_name='hashtag_id',
            new_name='hashtag',
        ),
        migrations.RenameField(
            model_name='posthashtag',
            old_name='post_id',
            new_name='post',
        ),
    ]
