# Generated by Django 4.2.7 on 2023-11-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='signature',
            field=models.CharField(default='What if man is not really a SCOUNDREL...', max_length=140),
        ),
    ]
