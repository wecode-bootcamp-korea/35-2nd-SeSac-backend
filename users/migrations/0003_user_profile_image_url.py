# Generated by Django 4.0.6 on 2022-08-03 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_kakao_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image_url',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
