# Generated by Django 4.2.10 on 2024-05-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
