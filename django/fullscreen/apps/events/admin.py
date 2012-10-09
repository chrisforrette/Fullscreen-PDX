from django.contrib import admin
from models import Event

class EventAdmin(admin.ModelAdmin):
    
    list_display = (
        'title',
        'when',
        'status',
    )
    
    date_hierarchy = 'when'
    list_filter = ('status',)
    list_editable = ('status',)

admin.site.register(Event, EventAdmin)