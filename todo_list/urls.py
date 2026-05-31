from django.urls import path, include

from todo_list.views import (
    index,
    TagList
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagList.as_view(), name="tag-list"),
]

app_name = 'todo_list'
