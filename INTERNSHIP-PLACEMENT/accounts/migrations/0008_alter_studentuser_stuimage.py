# Generated by Django 3.2.5 on 2021-08-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_studentuser_stuimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='stuImage',
            field=models.ImageField(default='user_profile1.png', null=True, upload_to='Images/'),
        ),
    ]
