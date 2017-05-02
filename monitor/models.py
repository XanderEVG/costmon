from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone

class Category(MPTTModel):
    title = models.CharField(max_length=300)   
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE) 
    
    class MPTTMeta:
        order_insertion_by = ['title']
    class Meta:
        verbose_name_plural = 'categories'
        
    #def import_logo_from_site()
    def __str__(self):
        return self.title

        
class City(models.Model):
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=5)
       
    class Meta:
        verbose_name_plural = 'cities'
        

    def __str__(self):
        return self.title
        
class AnalogItemsGroup(models.Model):
    title = models.CharField(max_length=200, blank=True)
    synonyms = models.CharField(max_length=2000, blank=True)
    
    #def get_items(self):
    def __str__(self):
        return self.title
        
class Competitor(models.Model):
    NONE = 'NON'
    COOKIE = 'COO'
    URL_DOMAIN = 'URD'
    URL_FOLDER = 'URF'
    URL_ALL = 'UAL'
    FULL = 'FUL'
    CITY_SELECT_METOD_CHOICES = (
        (NONE, ''),
        (COOKIE, 'Куки'),
        (URL_DOMAIN, 'URL(домен 3 уровня)'),
        (URL_FOLDER, 'URL(Подпапки)'),
        (URL_ALL, 'URL(Все)'),
        (FULL, 'Все'),
    )

    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=50)
    logo = models.FileField(upload_to='store_img/%Y/%m/%d', blank=True)
    url = models.URLField(blank=True)
        
    city_select_metod = models.CharField(max_length=3,
                                      choices=CITY_SELECT_METOD_CHOICES,
                                      default=NONE)
    
    
    #def import_logo_from_site()
    def __str__(self):
        return self.title
        
class Store(models.Model):
    сompetitor = models.ForeignKey(Competitor)
    city = models.ForeignKey(City)
    
    city_param = models.CharField(max_length=200, blank=True) 
    
    #def import_logo_from_site()
    def __str__(self):
        return '%s (%s)' % (self.сompetitor.title, self.city.short_title)
        
        

           
        
class Item(models.Model):
    sap_сode = models.CharField(max_length=200, blank=True)
    article = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    store = models.ForeignKey(Store, blank=True, null=True)
    #city = models.ForeignKey(City)
    category = models.ForeignKey(Category, blank=True, null=True)
    cost = models.DecimalField( max_digits=9, decimal_places=2, blank=True, null=True)
    img = models.URLField(blank=True) #models.FileField(upload_to='item_img/%Y/%m/%d', blank=True)
    analogs_items = models.ManyToManyField(AnalogItemsGroup, blank=True)
    url = models.URLField(blank=True)
    #city_cookie = models.CharField(max_length=40, blank=True)
    upload_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    