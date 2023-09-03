# Generated by Django 4.2.4 on 2023-09-03 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("P10", "0004_produtos_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produtos",
            name="desconto",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Produtos",
                to="P10.descontos",
            ),
        ),
        migrations.AlterField(
            model_name="produtos",
            name="sazonal",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Produtos",
                to="P10.sazonal",
            ),
        ),
    ]
