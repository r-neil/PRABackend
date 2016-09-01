from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date

from . import models
from . import serializers

def track():
	models.SiteView.objects.create()

class ListDirectTrains(APIView):
	def get(self, request, year, month, day, format=None):
		track()
		last_update_app = date(int(year), int(month), int(day))
		direct_trains = models.DirectTrain.objects.filter(effective_date__range=[last_update_app, date.today()])
	
		serializer = serializers.DirectTrainSerializer(direct_trains, many=True)
		return Response(serializer.data)
