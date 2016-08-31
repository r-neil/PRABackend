from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^((?P<month>[0-9]{2})-(?P<day>[0-9]{2})-(?P<year>[0-9]{4}))/$', views.ListDirectTrains.as_view(), name='direct_train_list'),
]