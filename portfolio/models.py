from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    skills = models.TextField()
    project_url = models.URLField()
    description = models.TextField()
    responsibilities = models.TextField()
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title