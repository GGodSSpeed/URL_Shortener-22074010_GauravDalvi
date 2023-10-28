# Generated by Django 4.2.6 on 2023-10-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URLdata",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("long_url", models.URLField()),
                ("short_code", models.TextField(null=True, unique=True)),
            ],
        ),
    ]