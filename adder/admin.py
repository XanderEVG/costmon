from django.contrib import admin

from .models import ImportItem
from .models import ImportedAnalogItem
from .models import ImportList

admin.site.register(ImportItem)
admin.site.register(ImportedAnalogItem)
admin.site.register(ImportList)