# loans/urls.py
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.LoanList.as_view(), name='loan_list'),
    url(r'^(?P<pk>\d+)/$', views.LoanDetail.as_view(), name='loan_detail'),
    url(r'^add/$', views.LoanCreateView.as_view(), name='loan_add'),
    url(r'^(?P<pk>\d+)/edit/$', views.LoanUpdateView.as_view(), name='loan_edit'),
]