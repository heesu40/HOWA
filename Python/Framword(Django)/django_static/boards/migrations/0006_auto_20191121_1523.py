# Generated by Django 2.2.7 on 2019-11-21 06:23

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20191121_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='boards/test2'),
        ),
    ]