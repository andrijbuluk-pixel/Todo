from django import forms

from todo_list.models import Tag, Task


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tag"
        ]


class TaskCreatedForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tag",
        ]

        widgets = {
            "deadline": forms.DateInput(
                attrs={"type": "date", "class": "form-control"},
                format="%Y-%m-%d",
            ),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TagCreatedForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
