from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ListDirectTrains.as_view(), name='direct_train_list'),
]