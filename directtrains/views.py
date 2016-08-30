from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

def track():
	models.SiteView.objects.create()

class ListDirectTrains(APIView):
	def get(self, request, format=None):
		track()
		direct_trains = models.DirectTrain.objects.all()
		serializer = serializers.DirectTrainSerializer(direct_trains, many=True)
		return Response(serializer.data)

