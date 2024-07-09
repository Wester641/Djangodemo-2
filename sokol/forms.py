from django import forms
from django.conf import settings
from .models import Projects


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'