from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
        """ ListAdmin Definition"""
        list_display = ("name","user","count_rooms")
