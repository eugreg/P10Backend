# Generated by Django 4.2.4 on 2023-08-09 19:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("usuario", "0002_usuario_nome_usuario_rg"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="nome",
        ),
    ]
