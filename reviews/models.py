from django.db import models
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStapedModel):

    """ Reiview model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    # 만약 유저를 삭제하면 그 객실에 관해서도 삭제해야한다.리뷰도 예외없다.
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    # Foreignkey가 정의 되어있어야만 value 값에 접근할 수 있다.
    def __str__(self):
        return f"{self.review} - {self.room}"

    # pront & backend 에서 모두 보이고싶은 기능이라면 model에서 한번에 정의하자
    # 함수를 만드는것 처럼 object와 연관있는 뭔가를 model에 만드는것이다.
    # round 함수 : 반올림한다 각각 인자를 (대상, 자릿수) 갖는다.
    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 1)

    rating_average.short_description = "Avg."
