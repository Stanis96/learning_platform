# Generated by Django 4.1.7 on 2023-03-12 12:48

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TopicsTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("topic", models.CharField(max_length=255, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="Tasks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("number", models.CharField(max_length=255, verbose_name="Number")),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("link", models.URLField(max_length=255, verbose_name="Link")),
                (
                    "difficulty",
                    models.PositiveSmallIntegerField(
                        default=None, null=True, verbose_name="Difficulty"
                    ),
                ),
                (
                    "count_solved",
                    models.PositiveSmallIntegerField(
                        default=None, null=True, verbose_name="Count Solved"
                    ),
                ),
                (
                    "topic",
                    models.ManyToManyField(
                        to="service_parsing_data.topicstask", verbose_name="Topic"
                    ),
                ),
            ],
            options={
                "verbose_name": "Task",
                "verbose_name_plural": "Tasks",
                "ordering": ("number", "title"),
            },
        ),
    ]