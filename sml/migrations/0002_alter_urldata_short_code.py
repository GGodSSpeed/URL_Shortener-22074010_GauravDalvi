# Generated by Django 4.2.6 on 2023-10-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sml", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urldata",
            name="short_code",
            field=models.TextField(max_length=15, null=True, unique=True),
        ),
    ]