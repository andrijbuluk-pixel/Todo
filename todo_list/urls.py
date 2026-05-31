from django.urls import path, include

from todo_list.views import (
    index,
    TagList,
    TagUpdate,
    TagDelete,
    TagCreate,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagList.as_view(), name="tag-list"),
    path("tags/created", TagCreate.as_view(), name="tag-created"),
    path("tags/<int:pk>/update/", TagUpdate.as_view(), name="tag-update"),
    path("tags/<int:pk>/deleta/", TagDelete.as_view(), name="tag-delete"),
]

app_name = 'todo_list'
