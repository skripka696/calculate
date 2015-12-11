from django.conf.urls import url, include
from views import index
import views

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    })

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^me/(?P<pk>\d+)/$', user_detail),

]
