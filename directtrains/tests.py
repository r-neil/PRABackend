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
		models.DirectTrain.objects.create(train_line=train_line[0], train_num='456', effective_date=date(2016,8,31))
		models.DirectTrain.objects.create(train_line=train_line[0], train_num='789', effective_date=date(2016,8,31))
		models.DirectTrain.objects.create(train_line=train_line[0], train_num='1234', effective_date=date(2016,8,31))
		models.DirectTrain.objects.create(train_line=train_line[0], train_num='5678', effective_date=date(2016,8,31))
		models.DirectTrain.objects.create(train_line=train_line[0], train_num='4567', effective_date=date(2016,8,31))
		
		self.factory = APIRequestFactory()
		self.view = views.ListDirectTrains.as_view()
		self.request = self.factory.get('')

	def tearDown(self):
		models.TrainLine.objects.all().delete()
		models.DirectTrain.objects.all().delete()

	def test_return_train_info(self):
		response = self.view(self.request, "1983","11","09")
		assert len(response.data) == models.DirectTrain.objects.count()

	def test_return_no_train_info(self):
		response = self.view(self.request, '2016','9','1')
		assert len(response.data) == 0

if __name__ == '__main__':
	unittest.main()