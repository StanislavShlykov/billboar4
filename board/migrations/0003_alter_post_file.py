# Generated by Django 4.2 on 2023-07-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to='my_downloads'),
        ),
    ]
