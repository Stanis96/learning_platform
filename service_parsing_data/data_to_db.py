from .models import Tasks
from .models import TopicsTask


def save_data_to_db(tasks: list) -> None:
    for task in tasks:
        topics = []
        for topic_name in task["topic"]:
            topic, _ = TopicsTask.objects.get_or_create(topic=topic_name)
            topics.append(topic)

        task_obj, created = Tasks.objects.get_or_create(
            number=task["number"],
            defaults={
                "title": task["title"],
                "link": task["link"],
                "difficulty": task["difficulty"],
                "count_solved": task["count_solved"],
            },
        )
        task_obj.topic.set(topics)
        task_obj.save()
