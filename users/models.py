from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	telephone = models.CharField(max_length = 15)

	#add any other applicable details later

	def __str__(self):
		return self.user.first_name
