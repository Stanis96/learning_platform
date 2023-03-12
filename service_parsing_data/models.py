from typing import Any

from django.db import models


class TopicsTask(models.Model):
    topic = models.CharField(max_length=255, null=False, verbose_name="Name")

    def __str__(self) -> Any:
        return self.topic

    def __repr__(self) -> str:
        return f"<Topic: {self.topic}>"


class Tasks(models.Model):
    number = models.CharField(max_length=255, null=False, verbose_name="Number")
    title = models.CharField(max_length=255, null=False, verbose_name="Title")
    link = models.URLField(max_length=255, null=False, verbose_name="Link")
    topic = models.ManyToManyField(TopicsTask, verbose_name="Topic")
    difficulty = models.IntegerField(null=True, default=None, verbose_name="Difficulty")
    count_solved = models.IntegerField(null=True, default=None, verbose_name="Count Solved")

    class Meta:
        ordering = ("number", "title")
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self) -> Any:
        return self.title

    def __repr__(self) -> str:
        return f"<Task: {self.title}>"
