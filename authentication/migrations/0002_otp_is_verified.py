# Generated by Django 4.1.4 on 2022-12-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="otp",
            name="is_verified",
            field=models.BooleanField(default=False),
        ),
    ]
