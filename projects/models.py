from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    github = models.URLField(max_length=500, blank=False)
    linkedin = models.URLField(max_length=500, blank=False)
    bio = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=False)
    github_url = models.URLField(max_length=500, blank=False)
    keyword = models.CharField(max_length=50, blank=False)
    key_skill = models.CharField(max_length=50, blank=False)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name
