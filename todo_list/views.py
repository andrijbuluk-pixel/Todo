from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import (
    TagForm,
    TagCreatedForm,
)

from todo_list.models import (
    Task,
    Tag,
)


def index(request):
    list_todo = Task.objects.all()

    return render(request, "todo_list/index.html", context={"todo_list": list_todo})


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
