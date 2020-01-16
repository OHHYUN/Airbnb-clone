from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Custom Item Admin """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Custom Room Admin """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Custom Photo Admin """

    pass
