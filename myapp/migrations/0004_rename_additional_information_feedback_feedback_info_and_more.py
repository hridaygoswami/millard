# Generated by Django 4.2.11 on 2024-04-19 12:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_alter_menu_items_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="feedback",
            old_name="additional_information",
            new_name="feedback_info",
        ),
        migrations.RemoveField(
            model_name="feedback",
            name="party_size",
        ),
    ]
