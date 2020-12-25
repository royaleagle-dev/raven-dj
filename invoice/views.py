from django.shortcuts import render, redirect
from invoice.models import Invoice
from django.utils import timezone
from django.views.generic import ListView
from django.views import View
from django.contrib import messages

class IndexView(View):
	
	def get(self, request):
		last_five_invoices = Invoice.objects.all().order_by('-transaction_date')
		ctx = {
		'last_five_invoices':last_five_invoices,
		}
		return render(request, "invoice/index.html", ctx)

	def post(self, request):
		pass

def addInvoice(request):
	if request.method == "POST":
		heading = request.POST.get('heading')
		amount = request.POST.get('amount')
		email = request.POST.get('email')
		transactionDate = request.POST.get('transactionDate')
		status = request.POST.get('status')
		description = request.POST.get('description')
		issuer = request.user.username
		date = request.POST.get('')

		status = int(status)
		if status == 1:
			status = 'p'
		else:
			status = 'u'

		new_invoice = Invoice(heading=heading, amount_due=amount, email=email, transaction_description=description,
			transaction_date=transactionDate, issuer=issuer, status=status)

		new_invoice.save()

		messages.success (request, "Invoice successfully Added")
		return redirect("invoice:index")

