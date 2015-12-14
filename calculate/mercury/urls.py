from django.conf.urls import url
from views import index
import views


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^me$', views.MeList.as_view()),

]
