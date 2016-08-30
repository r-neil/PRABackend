from rest_framework import serializers

from . import models

class DirectTrainSerializer(serializers.ModelSerializer):
	train_line = serializers.StringRelatedField(many=False)
	effective_date = serializers.DateTimeField(format='%m-%d-%Y')

	class Meta:
		fields = (
			'train_line',
			'train_num',
			'effective_date',
			)
		model = models.DirectTrain