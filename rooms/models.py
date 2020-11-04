from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class Room(core_models.TimeStapedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    # name은 필수사항이기때문에 null = True 나 Blank = True 를 사용할 수 없다.
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    # TimeField 와 DateField는 다르다
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # 다른 모델과 연결 : ForeignKey
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

