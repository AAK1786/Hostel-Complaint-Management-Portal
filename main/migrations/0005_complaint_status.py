# Generated by Django 4.1 on 2022-08-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_user_info_user_delete_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaint",
            name="status",
            field=models.CharField(default="pending", max_length=15),
        ),
    ]