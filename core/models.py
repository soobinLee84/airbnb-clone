from django.db import models


class TimeStampedModel(models.Model):

    """ Room Model Definition """

    """Model이 생성된 날짜를 구하려면 auto_now_add = True를 써주고
        auto_now = True는 새로운 날짜로 업데이트 해준다"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    """ If you didn't using this class, above models will be register for DB """

    class Meta:
        abstract = True