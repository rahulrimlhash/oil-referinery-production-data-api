# Generated by Django 4.2.1 on 2023-05-24 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="annualdata",
            name="api_number",
        ),
    ]
