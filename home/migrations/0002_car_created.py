# Generated by Django 4.2.4 on 2023-08-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]