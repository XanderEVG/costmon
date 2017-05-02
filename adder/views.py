from django.shortcuts import render
from django.http import HttpResponse
from .models import ImportItem
from .models import ImportedAnalogItem
from .models import ImportList

from monitor.models import City
from monitor.models import Category
from monitor.models import Competitor
from monitor.models import Store
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Count

def import_list(request, num_import=None):
    page=request.GET.get('page')
    import_list_obj=None
    if num_import is not None:
        if num_import.isdigit()==False:
            num_import=None
    if num_import is not None:
        try:
            import_list_obj = ImportList.objects.get(id=num_import)
        except ImportList.DoesNotExist:
            html_content = "Импорт с таким номером не существует"  
            HTTP_REFERER = reverse('import_list')            
            return render(request, 'fail.html', {'html_content':html_content, 'http_referer':HTTP_REFERER,})
        
    if page is None:
        page=1
    else:
        if page.isdigit()==False:
            page=1
    

    
    if import_list_obj is None:
        #Выводим все импорты
        
        imports=[];
        imports_objects=ImportList.objects.values('id', 'import_date', 'user__username', 'comment').annotate(items_count=Count('importitem')).order_by('-id')#[5:10]  
        for imob in imports_objects:
            if imob['user__username']   is not None:
                username = imob['user__username'] 
            else:
                username = ''
            imports.append({'import_id':imob['id'], 'import_date':imob['import_date'],'username':username,'comment':imob['comment'],'count':imob['items_count']})
            
        return render(request, 'adder/import_list.html', {'imports':imports,})

    else:
        #Выводим содержимое импорта
        
        items=[]
        import_id = import_list_obj.id
        import_date = import_list_obj.import_date
        if import_list_obj.user is None:
            import_autor = ''
        else:
            import_autor = import_list_obj.user.username
        import_comment = import_list_obj.comment
        item_objects=ImportedAnalogItem.objects.values( 'id',
                                                        'store__city__short_title', 
                                                        'store__сompetitor__short_title',                                                       
                                                        'url',
                                                        'import_item__id',
                                                        'import_item__sap_сode',                                                        
                                                        'import_item__article', 
                                                        'import_item__title',
                                                        'import_item__store__city__short_title', 
                                                        'import_item__store__сompetitor__short_title',                                                        
                                                        'import_item__url', 
                                                        'import_item__category__title',
                                                        'import_item__import_row_id') \
                                                        .filter(import_item__import_row_id=import_list_obj.id) \
                                                        .order_by('import_item__title', 'store__сompetitor__short_title', 'store__city__short_title') #[5:10]
        our_items=[]
        analog_items=[]
        
        for item_object in item_objects:
            new_item_id = item_object['import_item__id']
            
            new_analog_item = {
                                'parent_id':new_item_id,
                                'analog_id':item_object['id'],
                                'analog_store':"%s (%s)" % (item_object['store__сompetitor__short_title'],item_object['store__city__short_title']),
                                'analog_url':item_object['url']
            }

            new_item = {
                        'id':new_item_id,
                        'sap':item_object['import_item__sap_сode'],
                        'article':item_object['import_item__article'],
                        'title':item_object['import_item__title'],
                        'store': "%s (%s)" % (item_object['import_item__store__сompetitor__short_title'],item_object['import_item__store__city__short_title']),
                        'category':item_object['import_item__category__title'],
                        'url':item_object['import_item__url'],
                        
            }    
            if new_item not in our_items:
                our_items.append(new_item)
            analog_items.append(new_analog_item)
            
        for our_item in our_items:
            our_item_id = our_item['id']
            items.append({'our_item':our_item, 'analogs':[]})           
            for analog_item in analog_items:
                if analog_item['parent_id']==our_item_id:
                    items[-1]['analogs'].append(analog_item)    
                    
                       

        
        return render(request, 'adder/import_items_list.html', {
                                                            'items': items,                                                           
                                                            'import_id':import_id,
                                                            'import_date':import_date,
                                                            'import_autor':import_autor,
                                                            'import_comment':import_comment
        })
    
def add_page(request, num_import=None):
        
    if num_import is not None:
        if num_import.isdigit()==False:
            num_import=None
    if num_import is None:
        try:
            new_import = ImportList.objects.create(user=request.user) 
            new_import.save()
        except ImportList.FieldError:
            html_content = "Создать новый импорт не удалось"  
            HTTP_REFERER = reverse('import_list')            
            return render(request, 'fail.html', {'html_content':html_content, 'http_referer':HTTP_REFERER,})
        num_import=new_import.id
        url = reverse('add_page', kwargs={'num_import': num_import})
        return HttpResponseRedirect(url)
    else:    
        try:
            import_list_obj = ImportList.objects.get(id=num_import)
        except ImportList.DoesNotExist:
            html_content = "Импорт с таким номером не существует"  
            HTTP_REFERER = reverse('import_list')            
            return render(request, 'fail.html', {'html_content':html_content, 'http_referer':HTTP_REFERER,})
        import_date = import_list_obj.import_date
        if import_list_obj.user is None:
            import_autor = ''
        else:
            import_autor = import_list_obj.user.username
        import_comment = import_list_obj.comment   
        
    return render(request, 'adder/add_page.html', {'categories':Category.objects.all(),
                                                   'cities':City.objects.all(),
                                                   'competitors':Competitor.objects.exclude(id=settings.OUR_ORG_ID), #
                                                   'our_org': settings.OUR_ORG,
                                                   'num_import': num_import,
                                                   'import_date':import_date,
                                                   'import_autor':import_autor,
                                                   'import_comment':import_comment,
                                                  })
    
    
    
def item_edit(request, import_id, item_id):
    try:
        import_list_obj = ImportList.objects.get(id=import_id)
    except ImportList.DoesNotExist:
        html_content = "Импорт с таким номером не существует"  
        HTTP_REFERER = reverse('import_list')            
        return render(request, 'fail.html', {'html_content':html_content, 'http_referer':HTTP_REFERER,})
    import_date = import_list_obj.import_date
    if import_list_obj.user is None:
        import_autor = ''
    else:
        import_autor = import_list_obj.user.username
    import_comment = import_list_obj.comment   
        
      
    
    try:
        import_item = ImportItem.objects.get(id=item_id)
        item = {'id':import_item.id,
                    'sap': import_item.sap_сode,
                    'article': import_item.article,
                    'title': import_item.title,
                    'cat_id': import_item.category.id,
                    'cat_title': import_item.category.title,
                    'city_id': import_item.store.city.id,
                    'city_title': import_item.store.city.title,
                    'url': import_item.url,        
        }
        
    except ImportItem.DoesNotExist:
        html_content = "Обьект не найден"  
        HTTP_REFERER = reverse('import_list')            
        return render(request, 'fail.html', {'html_content':html_content, 'http_referer':HTTP_REFERER,})
        
    analogs_items_objs=ImportedAnalogItem.objects.values('id',
                                                        'store__сompetitor__id',
                                                        'store__сompetitor__short_title',                                                       
                                                        'url',
                                                        'import_item__id') \
                                                        .filter(import_item__id=import_item.id) \
                                                        .order_by('store__сompetitor__short_title')
    
    analogs_items=[]
    for analogs_items_obj in analogs_items_objs:
        analogs_items.append({
                                'id': analogs_items_obj['id'],
                                'comp_id': analogs_items_obj['store__сompetitor__id'],
                                'comp_title': analogs_items_obj['store__сompetitor__short_title'],
                                'url': analogs_items_obj['url'],
                                'impit_id': analogs_items_obj['import_item__id'],                       
        })
        
    return render(request, 'adder/add_page.html', {'categories':Category.objects.all(),
                                                   'cities':City.objects.all(),
                                                   'competitors':Competitor.objects.exclude(id=settings.OUR_ORG_ID), #
                                                   'our_org': settings.OUR_ORG,
                                                   'num_import': import_id,
                                                   'import_date':import_date,
                                                   'import_autor':import_autor,
                                                   'import_comment':import_comment,
                                                   'item':item,
                                                   'analogs_items':analogs_items
                                                  })
    
    
@csrf_protect     
def delete(request, import_id, item_id=-1):
    #Удалить все если задан id импорта
    #удалить товар, если задан id импорта и id товара
    html_content='ok'
    
    if item_id==-1:
        #delete all
        try:
            import_list_obj = ImportList.objects.get(id=import_id)
        except ImportList.DoesNotExist:
            html_content = "Импорт не существует"    
            return HttpResponse(html_content, content_type='text/html')
                #try:
        import_list_obj.delete()
                #except ImportList.:
                #    html_content = "fail: "    
                #    return HttpResponse(html_content, content_type='text/html')
        url = reverse('import_list')
        return HttpResponseRedirect(url)
    else:
        #delete item
        try:
            import_item_obj = ImportItem.objects.get(id=item_id)
        except ImportItem.DoesNotExist:
            html_content = "Обьект не найден"    
            return HttpResponse(html_content, content_type='text/html')
        import_item_obj.delete();        
    return HttpResponse(html_content, content_type='text/html')
    
@csrf_protect     
def delete_analog(request):
    analog_id = request.POST['analog_id']
    html_content = 'ok'
    try:
        analog_item_obj = ImportedAnalogItem.objects.get(id=analog_id)
    except ImportedAnalogItem.DoesNotExist:
        html_content = "Обьект не найден"    
        return HttpResponse(html_content, content_type='text/html')
    analog_item_obj.delete();        
    return HttpResponse(html_content, content_type='text/html')   
  
  
@csrf_protect  
def append(request):
    html_content="ok"
    item_id=int(request.POST['item_id'])
    num_import_val=request.POST['num_import']
    sap_code_val=request.POST['sap']
    article_val=request.POST['article']
    title_val=request.POST['title']
    category_id=request.POST['category']
    city_id=request.POST['city']
    url_val=request.POST['url']
    
    try:
        import_list_obj = ImportList.objects.get(id=num_import_val)
    except ImportList.DoesNotExist:
        html_content = "Импорт не существует"    
        return HttpResponse(html_content, content_type='text/html')
            
    try:
        city_val = City.objects.get(id=city_id)
    except City.DoesNotExist:
        html_content = "Город не существует"    
        return HttpResponse(html_content, content_type='text/html')
        
    try:
        our_org = Competitor.objects.get(short_title=settings.OUR_ORG)
    except Competitor.DoesNotExist:
        html_content = "Наша организация не определена или найдены дубли"     
        return HttpResponse(html_content, content_type='text/html')
    
    try:
        store_val = Store.objects.get(city=city_val, сompetitor=our_org)
    except Store.DoesNotExist:
        html_content = "Магазин не найден"     
        return HttpResponse(html_content, content_type='text/html')
        
    try:
        category_val = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        html_content = "Категория не найдена"       
        return HttpResponse(html_content, content_type='text/html')
    
    if item_id > 0:
        try:
            current_item = ImportItem.objects.get(id=item_id)
        except ImportItem.DoesNotExist:
            html_content = "Редактируемый обьект не найден"       
            return HttpResponse(html_content, content_type='text/html')
        current_item.edit(sap_сode=sap_code_val, article=article_val, title=title_val, store=store_val, category=category_val, url=url_val)
        
    else:
        item = ImportItem.objects.create(import_row=import_list_obj, sap_сode=sap_code_val, article=article_val, title=title_val, store=store_val, category=category_val, url=url_val)
        item.save()
    
    
    competitors = [(k[11:][:-1], v) for k, v in request.POST.items() if k.startswith('competitor[')]
    
    for competitor in competitors:
        analog_competitor_id=competitor[0]
        analog_url=competitor[1]
        
        try:
            analog_competitor = Competitor.objects.get(id=analog_competitor_id)
        except Competitor.DoesNotExist:
            continue
        
        try:
            analog_store = Store.objects.get(city=city_val, сompetitor=analog_competitor)
        except Store.DoesNotExist:
            continue
        
        if item_id > 0:
            try:
                current_analog_item = ImportedAnalogItem.objects.get(import_item=item_id, store=analog_store)
            except ImportedAnalogItem.DoesNotExist:      
                new_analog_item = ImportedAnalogItem.objects.create(import_item=current_item, store=analog_store, url=analog_url)
                new_analog_item.save()
                current_analog_item=None
            if current_analog_item:
                current_analog_item.edit(url=analog_url)
              
        else:
            new_analog_item = ImportedAnalogItem.objects.create(import_item=item, store=analog_store, url=analog_url)
            new_analog_item.save()
            return HttpResponse('current_analog_item NOT exist', content_type='text/html')
    
    
    return HttpResponse(html_content, content_type='text/html')
    
    
@csrf_protect  
def comment_save(request):
    html_content="ok"
    import_id=request.POST['id']
    comment=request.POST['comment']
    try:
        import_list_obj = ImportList.objects.get(id=import_id)
    except ImportList.DoesNotExist:
        html_content = "Импорт не существует"    
        return HttpResponse(html_content, content_type='text/html')
    import_list_obj.comment = comment
    import_list_obj.save()
    return HttpResponse(html_content, content_type='text/html')
    
    
    
    
    
    
    
    
    
    
    
    