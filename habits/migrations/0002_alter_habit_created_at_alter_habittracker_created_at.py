# Generated by Django 4.0.6 on 2022-07-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='habittracker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
