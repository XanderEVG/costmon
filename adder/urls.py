
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.import_list, name='import_list'),
    url(r'^(?P<num_import>\d+)$', views.import_list, name='import_list'),
    url(r'^add$', views.add_page, name='add_page'),
    url(r'^add/(?P<num_import>\d+)$', views.add_page, name='add_page'),
    url(r'^edit/(?P<import_id>\d+)/(?P<item_id>\d+)$', views.item_edit, name='import_item_edit'),
    url(r'^del/(?P<import_id>\d+)$', views.delete, name='delete'),
    url(r'^del/(?P<import_id>\d+)/(?P<item_id>\d+)$', views.delete, name='delete'),
    url(r'^del_analog$', views.delete_analog, name='delete_analog'), 
    url(r'^append$', views.append, name='append'),
    url(r'^save_comment$', views.comment_save, name='import_comment_save'),
]
