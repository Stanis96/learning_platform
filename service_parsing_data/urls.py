from django.urls import path

from .views import load_test_data_to_db


urlpatterns = [
    path("check/", load_test_data_to_db, name="Check"),
]
