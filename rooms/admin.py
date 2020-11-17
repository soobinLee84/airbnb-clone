from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass

# admin안의 admin이라고 보면된다.
class PhtoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """
    inlines = (PhtoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country","city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")},),
        (
            "More About the Space",
            {"fields": ("amenities", "facilities", "house_rules")},
        ),
        ("Last Details", {"fields": ("host",)},),
    )

    # 차례대로 정렬
    ordering = ("name", "price", "bedrooms")

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
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
        "city",
    )

    # foreign key를 좀 더 나은 방법으로 찾아 볼 수 있다.
    # 이경우엔 host를 검색하게 도와준다 (user admin 인터페이스를 제공함)
    raw_id_fields = ("host",)
    
    # icontains : 대소문자 구분이 없다 없어 그래 없다
    search_fields = ("=city", "^host__username")

    # filter_horizontal

    filter_horizontal = ("amenities", "facilities", "house_rules")

    # self : Rooomadmin
    # obj : 현재 row
    def count_amenities(self, obj):

        return obj.amenities.count()

    # count_amenities.short_description = "hello!"

    # phto 갯수 세기
    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photo Count"

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """" phot oAdmin description """

    
    list_display = ('__str__', 'get_thumbnail')

    # 사용자에게 썸네일을 여기 어드민 패널에서 보여줄것이다.
    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="60px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"