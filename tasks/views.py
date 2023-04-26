from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from tasks.models import Task


# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/taskcreate.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse("show_project", kwargs={"pk": self.object.project.pk})


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/tasklist.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
