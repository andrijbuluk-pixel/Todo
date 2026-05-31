from django.shortcuts import render
from django.views.generic import ListView

from todo_list.models import Task


def index(request):
    list_todo = Task.objects.all()

    return render(request, "todo_list/index.html", context={"todo_list": list_todo})


class TagList(ListView):
    model = Task
    context_object_name = "tag_list"
    template_name = "todo_list/tag_list.html"
