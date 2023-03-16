from django.db.models import QuerySet

from .models import Tasks
from .models import TopicsTask


def get_topics() -> QuerySet[TopicsTask]:
    topic_tasks = TopicsTask.objects.all()
    return topic_tasks


def get_difficulty(topic: str | None = None) -> list[str]:
    if topic:
        difficulties = (
            Tasks.objects.filter(topic__topic=topic)
            .values_list("difficulty", flat=True)
            .order_by()
            .distinct()
        )
    else:
        difficulties = Tasks.objects.all.values_list("difficulty", flat=True).order_by().distinct()
    return sorted([difficulty for difficulty in difficulties if difficulty is not None])
