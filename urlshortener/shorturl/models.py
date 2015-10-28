from django.db import models

# Create your models here.

"""class ViewManager(models.Manager):

    def filter_for_user(self, user):
        return self.filter(author=user)
"""

class Homepage(models.Model):
    # objects = ViewManager()

    @property
    def print_input(self):
        return(input())

