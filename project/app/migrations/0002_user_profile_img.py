# Generated by Django 5.0.6 on 2024-08-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
