# Generated by Django 4.2.5 on 2023-09-25 18:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_cadastro", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Usuarios",
            new_name="Usuario",
        ),
    ]