from django.http import HttpResponse

from .parser import parse_all_pages


def load_test_data_to_db(request):
    parse_all_pages()
    return HttpResponse("Data has been added!")
