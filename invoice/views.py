from django.shortcuts import render, redirect
from invoice.models import Invoice
from django.utils import timezone
from django.views.generic import ListView
from django.views import View

class IndexView(View):
	
	def get(self, request):
		last_five_invoices = Invoice.objects.all().order_by('-transaction_date')
		ctx = {
		'last_five_invoices':last_five_invoices,
		}
		return render(request, "invoice/index.html", ctx)

	def post(self, request):
		pass

