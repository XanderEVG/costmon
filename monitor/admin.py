from django.contrib import admin
from .models import Category
from .models import City
from .models import AnalogItemsGroup
from .models import Store
from .models import Item
from .models import Competitor

admin.site.register(Category)
admin.site.register(City)
admin.site.register(AnalogItemsGroup)
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Competitor)