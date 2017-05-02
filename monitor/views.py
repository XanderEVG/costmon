from django.shortcuts import render
from .models import Category
from .models import City
from .models import AnalogItemsGroup
from .models import Store
from .models import Item
from django.utils import timezone

def simple_products_table(request):
    current_city = City.objects.get(title='Тюмень')
    current_store = Store.objects.get(title='Строительный двор', city=current_city )
    items = Item.objects.filter(store=current_store).order_by('-modify_date') #[:10]
    return render(request, 'monitor/simple_products_table.html', {'items': items})
