# Generated by Django 3.0.7 on 2020-06-11 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0007_auto_20200612_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='tag',
            field=models.ManyToManyField(blank=True, to='log.Tags'),
        ),
    ]