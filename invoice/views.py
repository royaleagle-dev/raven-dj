from django.shortcuts import render, redirect
from invoice.models import Invoice
from django.utils import timezone
from django.views.generic import ListView

class InvoiceListView(ListView):
	model = Invoice
	context_object_name = 'invoices'
	template_name = 'index.html'

	def get_queryset(self):
		queryset = {
		'all': Invoice.objects.all().order_by('-transaction_date')
		}
		return queryset

