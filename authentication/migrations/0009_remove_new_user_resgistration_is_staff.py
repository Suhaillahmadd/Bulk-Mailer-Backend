# Generated by Django 4.1.4 on 2022-12-19 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0008_alter_new_user_resgistration_is_staff"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="new_user_resgistration",
            name="is_staff",
        ),
    ]