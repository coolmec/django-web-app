from django.contrib import admin

from listings.models import Band, Announce

# Register your models here.
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

class AnnounceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year', 'announce_type')

admin.site.register(Band, BandAdmin)
admin.site.register(Announce, AnnounceAdmin)