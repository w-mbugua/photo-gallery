# Generated by Django 3.2.3 on 2021-05-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='Location',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='photos',
            name='caption',
            field=models.CharField(max_length=200),
        ),
    ]