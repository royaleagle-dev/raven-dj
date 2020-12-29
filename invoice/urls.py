from django.urls import path
from . import views

app_name = 'invoice'

urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	path('addInvoice/', views.addInvoice, name = 'addInvoice'),
	path('invoices/', views.InvoiceListView.as_view(), name = 'invoices'),
	path('invoice-detail/<str:pk>', views.InvoiceDetail.as_view(), name = 'invoice-detail'),
	path('send-invoice/<str:id>', views.sendInvoice, name = 'send-invoice'),
	path('delete-invoice/<str:id>', views.deleteInvoice, name = 'delete-invoice'),
	path('trash/', views.TrashView.as_view(), name = 'trash'),
]