# Generated by Django 2.2.9 on 2022-03-16 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_auto_20220316_1955"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="group",
            options={"verbose_name_plural": "Группы"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-pub_date"], "verbose_name_plural": "Статьи"},
        ),
    ]
