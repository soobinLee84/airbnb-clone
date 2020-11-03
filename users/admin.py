from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
# @admin.register(models.User) 가 뜻하는 의미
# admin패널에서 이 user를 보고싶을때 user를 컨트롤한 클래스가 바로 이게 될것이다.
# 이것을 decorator라고하는데 class 위에 항상 위치 해 있어야 작동한다.

# 장고가 이미 만들어준 기능을 바로 여기 CustomerUserAdmin에 복붙해준다.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin"""

    # 기존에 setting 됫던것과 custermizing 했던것을 합친형태
    # admin.py에서 admin 패널의 구성을 바꿀 수 있다.(선택사항)
    # filedsets는 파란색 섹션이다.
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "gender",
                    "avatar",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    # list display : admin list에서 항목에 해당하는 리스트를 보여준다
    # list_display = ("username", "gender", "language", "email", "currency", "superhost")

    # list_filter : admin list에서 항목에 해당하는 필터링을 할 수있도록 구현 해 준다.
    # list_filter = ("superhost", "currency", "language")


# server가 실행되지 않아서 추가한 옵션
admin.site.unregister(models.User)
admin.site.register(models.User, CustomUserAdmin)

