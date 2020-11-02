from django.contrib import admin
from . import models


# Register your models here.
# @admin.register(models.User) 가 뜻하는 의미
# admin패널에서 이 user를 보고싶을때 user를 컨트롤한 클래스가 바로 이게 될것이다.
# 이것을 decorator라고하는데 class 위에 항상 위치 해 있어야 작동한다.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin"""

    # list_display = ("username", "gender", "language", "email", "currency", "superhost")
    # list_filter = ("superhost", "currency", "language")


# server가 실행되지 않아서 추가한 옵션
admin.site.unregister(models.User)
admin.site.register(models.User, CustomUserAdmin)

