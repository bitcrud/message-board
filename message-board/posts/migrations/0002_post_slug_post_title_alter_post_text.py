# Generated by Django 4.2.1 on 2023-05-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.CharField(
                blank=True, default="-", max_length=256, unique=True
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="title",
            field=models.TextField(default="-", max_length=256),
        ),
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.TextField(max_length=1024),
        ),
    ]