from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
# Create your models here.

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	telephone = models.CharField(max_length = 15)
	verification_code = models.CharField(default = '', max_length = 255)
	verified = models.IntegerField(default = 0,) #value of zero means unverified, and 1 means verified

	#add any other applicable details later

	def __str__(self):
		return self.user.username


	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user = instance, verification_code = uuid.uuid4())

	"""
	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
		"""