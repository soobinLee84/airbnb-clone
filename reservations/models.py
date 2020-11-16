from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.TimeStapedModel):

    """ Reservation model Definition """

    STATUS_PENDING = "pending"
    STUATS_CONFIRMED = "confirmed"
    STATUS_CANCLED = "cancled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STUATS_CONFIRMED, "confirmed"),
        (STATUS_CANCLED, "cancled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()

    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now <self.check_out

    #in_progress를 변경하고 싶다면, shortn description 써서 변경할 수 있다.
    in_progress.boolean = True