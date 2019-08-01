from django.db import models

# Create your models here.
class ActorModel(models.Model):
	Event=models.CharField(max_length=80)
	Actor=models.CharField(max_length=20)

	def __str__(self):
		return self.Event
		
