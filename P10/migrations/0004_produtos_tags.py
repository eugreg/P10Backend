# Generated by Django 4.2.4 on 2023-09-03 16:54

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("P10", "0003_categoria_materialcommunityicons"),
    ]

    operations = [
        migrations.AddField(
            model_name="produtos",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
