from django.db import models

class TrainLine(models.Model):
	train_line = models.CharField(max_length=20)

	def __str__(self):
		return '{}'.format(self.train_line)

class DirectTrain(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)

	train_line = models.ForeignKey(TrainLine)
	train_num = models.CharField(max_length=20)
	effective_date = models.DateField()
	

	def __str__(self):
		return '{} - {}: {}'.format(self.effective_date, self.train_line, self.train_num)

class SiteView(models.Model):
	viewed_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}'.format(self.viewed_at)


