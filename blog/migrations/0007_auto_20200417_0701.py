# Generated by Django 3.0.5 on 2020-04-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200417_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.FileField(blank=True, upload_to='img'),
        ),
    ]
