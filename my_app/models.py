from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Something specific leaned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # this command tells django, whenever a topic is deleted all entry related to that should also be deleted,
    # this is known as cascading delete.

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Metaclass contains extra information about a model class such as 1.db_table 2.ordering 3.human-readable names for models etc... """
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.text[:50]}"
