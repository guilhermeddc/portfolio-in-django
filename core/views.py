from django.shortcuts import render
from django.views import generic
from .models import Profile, Projects


class ProjectListView(generic.ListView):
    model = Projects
    template_name = 'index.html'
    context_object_name = 'project_list'
    paginate_by = 3


index = ProjectListView.as_view()
