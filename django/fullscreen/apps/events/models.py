from django.db import models
from fullscreen.apps.machete.models import GlobalModel
from fullscreen.apps.machete.google_maps import find_geo

EVENT_CATEGORY_CHOICES = (
    ('am', 'Fullscreen AM',),
    ('pm', 'Fullscreen PM',),
)

class Event(GlobalModel):
    
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, db_index=True, choices=EVENT_CATEGORY_CHOICES)
    when = models.DateTimeField()
    image = models.ImageField(upload_to='events', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    host_name = models.CharField('Host Name', max_length=255, blank=True, null=True)
    host_url = models.URLField('Host URL', blank=True, null=True)
    host_address = models.CharField('Host Address', max_length=255, blank=True, null=True)
    host_longitude = models.FloatField('Host Longitude', db_index=True, blank=True, null=True, editable=False)
    host_latitude = models.FloatField('Host Latitude', db_index=True, blank=True, null=True, editable=False)
    
    registration_url = models.URLField('Registration URL', blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):

        """
        If no longitude/latitude present, try to hit Google maps and see if we can find 'em
        """

        if not self.host_longitude and not self.host_latitude:
            
            
            point = find_geo(self.host_address)
            
            if point:

                coords = point['Placemark'][0]['Point']['coordinates']

                # Store longitude/latitude

                self.host_longitude = coords[0]
                self.host_latitude = coords[1]

        super(Event, self).save(*args, **kwargs)