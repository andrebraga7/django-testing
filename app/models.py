from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    assigned = models.CharField(max_length=15, default='Unassigned')

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('is_manager', 'Is manager'),
            ('is_employee', 'Is employee'),
            ('is_client', 'Is client')]
