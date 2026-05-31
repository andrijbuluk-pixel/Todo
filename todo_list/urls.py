from django.urls import path, include

from todo_list.views import (
    index
)

urlpatterns = [
    path("", index, name="index"),
]

app_name = 'todo_list'
