from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^currencies$', views.CurrenciesView.as_view(), name='currencies'),
    url(r'^associations$', views.AssociationView.as_view(), name='associations'),
    url(r'^certifications', views.CertificationView.as_view(), name='certifications'),
    url(r'^locations$', views.LocationView.as_view(), name='locations'),
    url(r'^me$', views.MeView.as_view()),
    url(r'^ports$', views.PortView.as_view(), name='ports'),
    url(r'^accounts/user/$', views.CorporateaccountList.as_view(), name='user-account-list'),
]
