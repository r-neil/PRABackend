from django.contrib import admin

from . import models

class DirectTrainAdmin(admin.ModelAdmin):
	list_display = ['train_line', 'train_num', 'effective_date']
	#list_editable = ['already_used']

class TrainLineAdmin(admin.ModelAdmin):
	list_display = ['train_line']

class SiteViewAdmin(admin.ModelAdmin):
	list_display = ['viewed_at']


admin.site.register(models.DirectTrain, DirectTrainAdmin)
admin.site.register(models.TrainLine, TrainLineAdmin)
admin.site.register(models.SiteView, SiteViewAdmin)