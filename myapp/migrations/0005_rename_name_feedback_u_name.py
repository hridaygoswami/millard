# Generated by Django 4.2.11 on 2024-04-19 12:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_rename_additional_information_feedback_feedback_info_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="feedback",
            old_name="name",
            new_name="u_name",
        ),
    ]
