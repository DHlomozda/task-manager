from django import forms
from django.contrib.auth.forms import UserCreationForm

from task.models import Task, Worker


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        )
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "is_completed",
            "priority",
            "task_type",
            "assignees"
        )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )

class WorkerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "position")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ("password1", "password2"):
            self.fields[name].widget.attrs.update({"class": "form-control"})
