# Generated by Django 3.2.9 on 2022-02-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluckbuster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='technology',
            field=models.CharField(max_length=20, null=True),
        ),
    ]