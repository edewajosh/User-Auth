# Generated by Django 3.1.1 on 2021-01-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210108_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default=models.CharField(max_length=50), max_length=50),
        ),
    ]
