from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    """ Extend Client Model"""

    client_name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name


class CustomUser(models.Model):
    """ Extend Customuser Model"""

    project = models.CharField(max_length=50,null=True, blank=True)
    user = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.project


class Project(models.Model):
    """ Extend Project Model"""

    project_name = models.CharField(max_length=100, blank=False, unique=True)
    clients = models.CharField(max_length=50,unique=True)
    users = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                    related_name='project_created_by')





