from django.db import models


class Projects(models.Model):
    img = models.ImageField(upload_to='media/')