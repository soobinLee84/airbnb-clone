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

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    # Meta class란 모델내의 모든 class들 안에 있는 class 다
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    # 정말 고맙게도 장고는 복수형을 자동으로 붙여준다 하지만
    # 때에 따라 복수형이 달라지기 때문에
    # Meta class의 attribute인 verbose_name_plural 을 따로 써서 설정해준다.
    class Meta:
        verbose_name_plural = "Facilites"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStapedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_phtos")
    # Room 이 지워지면 사진도 연결되어있기 때문에 함께 지워져야 함 그러니 CASCADE
    # python은 위에서 아래로 읽기때문에 Photo class를 아래로 위치하게 해야하지만
    # 이것은 번외로 스트링값으로 바꾸면 굳이 위치를 바꿀 필요가 없다.
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    # Foreignkey 오직 한가지 타입만 가진다. room type을 삭제해도 room을 삭제하고싶지 않다!
    # 한사람만 객실유형을 설정할 수 있는건 아니기 때문에 일단 null 처리한다.
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    # 다대 다 관계 : 여러 entity가 관계를 이룬다.
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwarags):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwarags)

    # 프론트 뿐만아니라 백 단에 서도 리뷰의 평점을 보고싶기 때문에 모델에서 함수를 정의한다.
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if not len(all_reviews):
            return "No reviews"
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)

