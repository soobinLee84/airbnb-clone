from django.db import models


class TimeStapedModel(models.Model):

    """ Time stamped Model """

    # class DateField(auto_now = True, auto_now_add=False)
    # auto now가 true이면 필드가 Model을save할 때 date랑 time을 기록한다.
    # auto now_add 가 true이면 Model를 생성할 때마다 수시로 업데이트 된다

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 위 모델들이 데이터베이스에 등록되지않기를 원한다. 그럴땐 metaclass를 사용한다
    class Meta:
        abstract = True

