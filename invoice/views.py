from django.shortcuts import render, redirect
from invoice.models import Invoice
from django.utils import timezone
from django.views.generic import ListView
from django.views import View

class IndexView(View):
	
	def get(self, request):
		pass

	def post(self, request):
		pass

