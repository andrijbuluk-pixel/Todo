from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import (
    TagForm,
    TagCreatedForm,
    TaskCreatedForm,
    TaskUpdateForm,
)

from todo_list.models import (
    Task,
    Tag,
)


def index(request):
    list_todo = Task.objects.all().order_by("-datetime")


    return render(request, "todo_list/index.html", context={"todo_list": list_todo})


class TaskCreate(generic.CreateView):
    model = Task
    form_class = TaskCreatedForm
    success_url = reverse_lazy("todo_list:index")


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("todo_list:index")


class TaskDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")


class TagList(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo_list/tag_list.html"


class TagCreate(generic.CreateView):
    model = Tag
    form_class = TagCreatedForm
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdate(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo_list:tag-list")


class TagDelete(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")


class TaskToggleView(generic.View):
    def post(self, request, pk):
        obj = Task.objects.get(pk=pk)
        obj.done = not obj.done
        obj.save()

        return redirect("todo_list:index")
