from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^currencies$', views.CurrenciesView.as_view(), name='currency'),
    url(r'^associations$', views.AssociationView.as_view(), name='association'),
    url(r'^certifications', views.CertificationView.as_view(), name='certification'),
    url(r'^locations$', views.LocationView.as_view(), name='location'),
    url(r'^me$', views.MeList.as_view()),
]
