from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from projects.models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/projectlist.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/projectdetail.html"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/projectcreate.html"
    fields = ["name", "description", "members"]

    def get_success_url(self):
        return reverse("show_project", kwargs={"pk": self.object.pk})
