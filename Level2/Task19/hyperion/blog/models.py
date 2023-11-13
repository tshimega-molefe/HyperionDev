from django.db import models


# Create your models here.
class Post(models.Model):
    # Create the primary keys, i.e. headings for each column in the database table
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()


def __str__(self):
    return self.title
