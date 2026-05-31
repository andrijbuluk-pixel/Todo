from django.shortcuts import render

from todo_list.models import Task


def index(request):
    list_todo = Task.objects.all()

    return render(request, "todo_list/index.html", context={"todo_list": list_todo})