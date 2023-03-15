from celery import shared_task

from .parser import parse_all_pages


@shared_task
def parse_all_pages_task():
    parse_all_pages()
