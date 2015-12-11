from django.conf.urls import url
from . import views

list_currency = views.CurrenciesViewSet.as_view(actions={'get': 'list'})
detail_currency = views.CurrenciesViewSet.as_view(actions={'get': 'retrieve'})
list_association = views.AssociationViewSet.as_view(actions={'get': 'list'})
detail_association = views.AssociationViewSet.as_view(actions={'get': 'retrieve'})

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^currencies$', list_currency, name='currency'),
    url(r'^currencies/(?P<pk>[0-9])$', detail_currency),
    url(r'^associations$', list_association, name='association'),
    url(r'^associations/(?P<pk>[0-9])$', detail_association),
]
