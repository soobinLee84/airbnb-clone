from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    list_display = (
        "name",
        "host",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = ("instant_book", "city", "country")
    # icontains : 대소문자 구분이 없다 없어 그래 없다
    search_fields = ("=city", "^host__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """" photoAdmin description """

    pass

