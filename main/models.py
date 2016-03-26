from django.db import models
from django.utils import timezone

# Create your models here.


class Post (models.Model):
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=200)
	text =models.TextField()
	created_time = models.DateTimeField(default=timezone.now)
	publshed_date = models.DateTimeField(blank=True,null=True)


	def publish (self):
		publish_date = timezone.now()
		self.save()

	def __unicode__ (self):
		return self.title

