from django.shortcuts import render, redirect, get_object_or_404
from invoice.models import Invoice
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail

class IndexView(View):
	
	def get(self, request):
		last_five_invoices = Invoice.objects.filter(trashed__exact = False).order_by('-transaction_date')[:5]
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

class InvoiceListView(ListView):
	template_name = "invoice/invoices.html"
	context_object_name = 'invoices'
	model = Invoice

	def get_queryset(self):
		queryset = {
			'all':Invoice.objects.filter(trashed__exact = False),
		}
		return queryset

class InvoiceDetail(DetailView):
	template_name = 'invoice/invoice-detail.html'
	context_object_name = 'invoice'
	model = Invoice

def sendInvoice(request, id):
	invoice = get_object_or_404(Invoice, id=id)
	invoice.sent = True

	pay_link = 'localhost/invoice/invoice-detail/{0}'.format(invoice.id)
	msg = f"{invoice.transaction_description}: Amount Due {invoice.amount_due}. Sent Today {timezone.now()}. \
	Payment Link: {pay_link}"

	send_mail(
		subject = invoice.heading,
		message = msg,
		from_email = 'ayo@ayo.com',
		recipient_list = ['titi@titi.com'],
	)

	invoice.save()
	return redirect('invoice:invoice-detail', pk=id)

def deleteInvoice(request, id):
	invoice = get_object_or_404(Invoice, id=id)
	invoice.trashed = True
	invoice.save()
	messages.success(request, "Invoice successfully trashed")
	return redirect('invoice:index')

class TrashView(View):
	def get(self, request):
		trashed_invoices = Invoice.objects.filter(trashed__exact = True)
		ctx = {
		'trashed_invoices':trashed_invoices,
		}
		return render(request, "invoice/trash.html", ctx)
	def post(self, request):
		pass

