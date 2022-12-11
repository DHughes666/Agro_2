from django.contrib import admin
from .models import Incidence, Swamp, Airport
from leaflet.admin import LeafletGeoAdmin

# Register your models here.


class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


class SwampAdmin(LeafletGeoAdmin):
    list_display = ('f_code', 'f_codedesc')


class AirportAdmin(LeafletGeoAdmin):
    list_display = ('name', 'use')


admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(Swamp, SwampAdmin)
admin.site.register(Airport, AirportAdmin)
