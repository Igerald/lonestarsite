from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    info_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name






  #  video = EmbedVideoField()

    


'''
        {% for i in obj %}
            {% video i.video 'small' %}
        {% endfor %}

'''