from django.db import models
from django.utils import timezone
from monitor.models import Store
from monitor.models import Category
from django.contrib.auth.models import User

class ImportList(models.Model):
    import_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True)
    comment = models.CharField(max_length=400, blank=True, null=True, default='')
    
    def __str__(self):
        if self.user is not None:
            return '%s) %s (%s)' % (self.id, self.user.username, self.import_date.strftime('%Y-%m-%d %H:%M'))
        else:
            return '%s) %s' % (self.id, self.import_date.strftime('%Y-%m-%d %H:%M'))    

class ImportItem(models.Model):
    import_row = models.ForeignKey(ImportList, blank=True, null=True) #, on_delete=models.CASCADE
    sap_сode = models.CharField(max_length=200, blank=True)
    article = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    store = models.ForeignKey(Store, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    url = models.URLField(blank=True)

    
    def __str__(self):
        return self.title
        
    def edit(self, sap_сode, article, title, store, category, url):
        self.sap_сode = sap_сode
        self.article = article
        self.title = title
        self.store = store
        self.category = category 
        self.url = url
        self.save()
        
class ImportedAnalogItem(models.Model):
    import_item = models.ForeignKey(ImportItem, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, blank=True, null=True)
    url = models.URLField(blank=True)
    
    def __str__(self):
        return '%s (%s)' % (self.import_item.title, self.store)
        
    def edit(self, url):
        self.url = url
        self.save()