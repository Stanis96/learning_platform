from django.contrib import admin

from .models import Tasks
from .models import TopicsTask


admin.site.register(Tasks)
admin.site.register(TopicsTask)
