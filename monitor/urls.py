
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.simple_products_table, name='simple_products_table'),
]
