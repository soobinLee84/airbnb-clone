from django.db import models
from core import models as core_models


class List(core_models.TimeStapedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    # 만약 유저가 삭제되면 리스트에서도 사라져야 하므로 CASCADE!
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"