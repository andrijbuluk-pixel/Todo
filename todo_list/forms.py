from django import forms

from todo_list.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TagCreatedForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]