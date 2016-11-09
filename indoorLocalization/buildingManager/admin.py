from django.contrib import admin
from .models import Buildings, Campuses, Floors, PointOfInterests


admin.site.register(Campuses)
admin.site.register(Buildings)
admin.site.register(Floors)
admin.site.register(PointOfInterests)
