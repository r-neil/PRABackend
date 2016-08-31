from django.test import TestCase
import unittest
from rest_framework.test import APIRequestFactory
from datetime import date

from . import views
from . import models

class GetRequestTest(unittest.TestCase):

	def setUp(self):
		models.TrainLine.objects.create(train_line='Thorn')
		train_line = models.TrainLine.objects.all()

		models.DirectTrain.objects.create(train_line=train_line[0], train_num='123', effective_date=date(2016,8,31))

	def test_new_app_better(self):
		factory = APIRequestFactory()
		view = views.ListDirectTrains.as_view()
		request = factory.get('')
		response = view(request, "1983","11","09")
		response.render()
		print("count is: {}".format(response.content.count))
		print("data is: {}".format(response.content))
		assert len(response.content) > 0

if __name__ == '__main__':
	settings.configure()
	unittest.main()