# Generated by Django 3.2.5 on 2021-08-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20210813_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipinfo',
            name='pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='placementinfo',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]
