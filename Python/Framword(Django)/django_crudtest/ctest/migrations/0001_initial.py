# Generated by Django 2.2.7 on 2019-11-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ctest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('new_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
