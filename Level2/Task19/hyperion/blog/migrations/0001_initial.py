# Generated by Django 4.2.7 on 2023-11-13 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
