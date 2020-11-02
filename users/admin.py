from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass


# server가 실행되지 않아서 추가한 옵션
admin.site.unregister(models.User)
admin.site.register(models.User, CustomUserAdmin)

