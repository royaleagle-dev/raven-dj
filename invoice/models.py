from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

class Invoice(models.Model):
	id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
	heading = models.CharField(max_length = 255)
	amount_due = models.IntegerField(default = 0)
	email = models.EmailField()
	transaction_description = models.TextField(max_length = 2000)
	transaction_date = models.DateTimeField(default = timezone.now)
	issuer = models.CharField(max_length = 255)  #Issuer must be a registered user
	status_choices = (
		('p', 'paid'),
		('u', 'unpaid')
	)
	status = models.CharField(max_length = 1, choices = status_choices, default = 'u')

	def __str__(self):
		return str(self.id)



