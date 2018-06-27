from django.db import models
from django.contrib.auth.models import User
	
class Events(models.Model):
	event_name = models.CharField(max_length=20)
	day = models.CharField(max_length=20)
	timing = models.CharField(max_length=20)
	slotid=models.IntegerField(default=0)
	count = models.IntegerField(default=100)
	
	
class Booked_slot(models.Model):
	user=models.ForeignKey(User)
	evname=models.CharField(max_length=20)
	event = models.ForeignKey(Events)
