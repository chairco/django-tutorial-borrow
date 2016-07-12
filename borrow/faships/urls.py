# faships/urls.py
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required

from . import views


urlpatterns = [
    url(r'^$', views.FashipList.as_view(), name='faship_list'),
    url(r'^(?P<pk>\d+)/$', views.FashipDetail.as_view(), name='faship_detail'),
    url(r'^add/$', login_required(views.FashipCreateView.as_view()), name='faship_add'),
    url(r'^(?P<pk>\d+)/edit/$', views.FashipUpdateView.as_view(), name='faship_edit'),
]