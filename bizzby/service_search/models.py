from __future__ import unicode_literals

from django.db import models

class Service(models.Model):
    # name: servicer name, e.g. cleaner, plumber, etc.
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    # description: summary of task, e.g. "fit a washing machine"
    # price: cost of task. Allows values up to 999,999.99
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    service = models.ForeignKey('Service')

    def __unicode__(self):
        return self.description
