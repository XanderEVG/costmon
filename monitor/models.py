from django.db import models
from django.utils import timezone


class Items(models.Model):
    id
    sap_сode
    article
    title
    synonyms #?
    description
    city  #id
    category
    parent_item #?
    cost
    img
    analogs_items #?
       
    
    
    
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title