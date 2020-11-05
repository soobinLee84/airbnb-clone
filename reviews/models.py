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
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    # Foreignkey가 정의 되어있어야만 value 값에 접근할 수 있다.
    def __str__(self):
        return f"{self.review} - {self.room}"
