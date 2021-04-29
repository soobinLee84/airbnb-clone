from django.db import models


class TimeStampedModel(models.Model):

    """ Room Model Definition """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    """ If you didn't using this class, above models will be register for DB """

    class Meta:
        abstract = True