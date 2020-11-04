from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# AbstractItem이 필요한이유는 카테고리만 다를뿐
# 카테고리마다 item이 들어가기 때문이다
class AbstractItem(core_models.TimeStapedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition """

    pass


class Amemity(AbstractItem):

    """Amenity Model Definition"""

    pass


class Facility(AbstractItem):

    """ Facility Model Definition """

    pass


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    pass


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
    # 한 모델과 다른 모델과 연결시켜주는 역할 : ForeignKey
    # CASADE : casade deletes. Django emluates the behavior of SQL constrait
    #          ON DELETE CASADE and also deletes the object containg the ForeignKey
    # CASADE는 폭포수로 부모가 삭제되면 자식들도 함께 삭제되는 폭포수 효과를 말한다.
    # 쉽게말해 유저가 삭제되면 유저가 올린 room이 함께 삭제된다는뜻
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # Foreignkey 오직 한가지 타입만 가진다. room type을 삭제해도 room을 삭제하고싶지 않다!
    # 한사람만 객실유형을 설정할 수 있는건 아니기 때문에 일단 null 처리한다.
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    # 다대 다 관계 : 여러 entity가 관계를 이룬다.
    amenities = models.ManyToManyField(Amemity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
