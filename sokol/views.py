from django.shortcuts import render
from .forms import ProjectsForm
from .models import Projects


def home(request):
    if request.POST == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            projects = Projects.objects.all()
    else:
        form = ProjectsForm()
        projects = Projects.objects.all()
    return render(request, 'home.html', {'form': form, 'projects': projects})