from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^ports$', views.PortList.as_view({'get': 'list'}), name='port-list'),
    url(r'^ports/(?P<pk>[0-9])$', views.PortList.as_view({'get': 'retrieve'}), name='port-detail'),
    url(r'^$', views.index, name='index'),

]
